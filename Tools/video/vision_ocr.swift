import AppKit
import Foundation
import Vision

struct OCRBlock: Encodable {
    let text: String
    let confidence: Float
}

struct OCRResult: Encodable {
    let path: String
    let text: String
    let mean_confidence: Float
    let blocks: [OCRBlock]
    let error: String?
}

func emit(_ result: OCRResult) {
    let encoder = JSONEncoder()
    encoder.outputFormatting = []
    if let data = try? encoder.encode(result), let line = String(data: data, encoding: .utf8) {
        print(line)
    }
}

for rawPath in CommandLine.arguments.dropFirst() {
    let path = (rawPath as NSString).expandingTildeInPath
    guard let image = NSImage(contentsOfFile: path) else {
        emit(OCRResult(path: path, text: "", mean_confidence: 0, blocks: [], error: "cannot_open_image"))
        continue
    }

    var rect = CGRect(origin: .zero, size: image.size)
    guard let cgImage = image.cgImage(forProposedRect: &rect, context: nil, hints: nil) else {
        emit(OCRResult(path: path, text: "", mean_confidence: 0, blocks: [], error: "cannot_create_cgimage"))
        continue
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["zh-Hans", "en-US"]

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    do {
        try handler.perform([request])
    } catch {
        emit(OCRResult(path: path, text: "", mean_confidence: 0, blocks: [], error: String(describing: error)))
        continue
    }

    let observations = request.results ?? []
    var blocks: [OCRBlock] = []
    for observation in observations {
        if let candidate = observation.topCandidates(1).first {
            let text = candidate.string.trimmingCharacters(in: .whitespacesAndNewlines)
            if !text.isEmpty {
                blocks.append(OCRBlock(text: text, confidence: candidate.confidence))
            }
        }
    }

    let text = blocks.map { $0.text }.joined(separator: "\n")
    let meanConfidence: Float
    if blocks.isEmpty {
        meanConfidence = 0
    } else {
        meanConfidence = blocks.map { $0.confidence }.reduce(0, +) / Float(blocks.count)
    }

    emit(OCRResult(path: path, text: text, mean_confidence: meanConfidence, blocks: blocks, error: nil))
}

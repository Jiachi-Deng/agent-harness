---
title: "Ultimate Beginner Guide to Learning ComfyUI (2026)"
source: "https://www.youtube.com/watch?v=l4CiwGS2ewY"
author:
  - "[[Max Novak]]"
published: 2026-04-30
created: 2026-05-23
description: "Ultimate Beginner Guide to Learning ComfyUI (2026)------------------------------------------------------------------------------------------Learn more about NVIDIA Studio here! : https://nvda.ws/4vZ"
tags:
  - "clippings"
compile_status: compiled
compiled_to:
  - "Wiki/AI视频制作/ComfyUI本地视频生成入门.md"
  - "Wiki/AI视频制作/AI短剧与漫剧制作流水线.md"
  - "Outputs/SOP与模板/AI视频短剧制作检查清单.md"
remaining_value: medium
---
![](https://www.youtube.com/watch?v=l4CiwGS2ewY)

Ultimate Beginner Guide to Learning ComfyUI (2026)  
\------------------------------------------------------------------------------------------  
Learn more about NVIDIA Studio here! : https://nvda.ws/4vZMU9f  
📩 (business inquiries: sawickimx@gmail.com)  
\------------------------------------------------------------------------------------------  
RESOURCES:  
Download the workflow for free 👉 https://www.dropbox.com/scl/fi/ko0l707206ver40p02533/Flux2-Klein-Style-Transfer-Upscale.json?rlkey=s55r4793w4wey4sqbw83edmc8&st=wj5ab0x5&dl=0  
  
Check out another comfy tutorial I made and more free workflows on the @NVIDIA-Studio channel here: (https://youtu.be/tuXveeHJpDA?si=M2BCQEffl3X1HlFi)  
  
Install Comfy:  
https://www.comfy.org/  
  
Nvidia SuperRes upscale node:  
https://github.com/Comfy-Org/Nvidia\_RTX\_Nodes\_ComfyUI  
  
Today I'll be walking your through a beginner guide to learning comfy ui. we'll go over installation, use cases, and beginner image and video workflows.  
  
  
  
TIMESTAMPS:  
0:00 - Intro  
0:19 - What you can do with ComfyUI  
1:00 - Recommended hardware  
2:00 - Installation  
5:00 - Models & Custom Nodes  
6:00 - Video creation workflow for beginners (LTX)  
12:00 - Simplest way to understand how it works  
13:50 - Upscaling with Nvidia SuperRes Node  
16:00 - Other video workflow mentions  
16:50 - Image creation workflow for beginners (workflow included)  
  
  
#comfyui #wan2.2 #flux

## Transcript

### Intro

**0:00** · What's going on, guys? Today, I'm going to share with you my ultimate guide for learning Comfy UI. I'll show you what it is, how to get it running on your machine and what you can do with it, starting with your very first generation all the way to the kind of stuff professionals are using it for right now. So, I want to start with the why because the best way to understand why this tool matters is to see what people are actually building with it. So, everything you just saw use CompuI in some way, shape, or form. And the best part is it is completely free. It's open source and it runs locally on your own hardware.

### What you can do with ComfyUI

**0:31** · That means no subscriptions, no cloud fees, no waiting in AQ. And because it's node-based, you're also getting total control over every part of the generation pipeline. So that all sounds great, but of course, because the tool is running locally, I recommend you have the hardware to run everything smoothly to get the best experience. So, speaking of hardware, this video is sponsored by Nvidia, and it's a natural fit because CUDA, Nvidia's GPU computing platform, is what Comfy UI is using under the hood for fast inference.

**0:59** · The better your GPU, the faster you generate. So, here is a rough breakdown of my recommendations. To be able to handle most image models as well as some video models with optimization flags, I recommend at least 8 gigabytes VRAM.

### Recommended hardware

**1:15** · Things like an RTX 3060 or 4060 for a nice middle ground sweet spot that can handle most everything comfortably. I recommend at least 12 to 16 GB of VRAM for your GPU. And to be able to run the biggest models with zero compromise, minimum 24 GB of VRAM, something like a 4090 or a 5090, which is what I'm using personally. Now, if you don't have a dedicated GPU, don't panic. There are some cloud GPU options like RunPod that let you rent time by the hour.

**1:41** · I'll link some guides to getting set up with Comfy UI and Runpod specifically down below if you would like to take that route. All right, so let's walk through how to actually install Comfy UI. So, first things first, we want to go to the Comfy UI GitHub or just go to the comfyui.org website and you'll be able to find all of the installation links from there.

### Installation

**2:02** · I'm going to go and download the latest Windows portable build. You can also go with the desktop build. It's kind of personal preference. So, extract that somewhere with plenty of space. And then once you've extracted it, let's go ahead and click into the folder structure and I'll walk you through some things you need to know. So, you're going to have your models folder where you can place all of the AI models that we download.

**2:22** · There are subfolders for that where you can place in Laura's upscale models or any other necessary component or extension. So, for now, I don't want to confuse you. Just know that this is where this file structure exists and you may need to go and reference it if something isn't working in the future.

**2:35** · There are a lot of things to make your life easier like the Comfy UI manager.

**2:39** · So, we're going to actually go and install that first because it'll make things like installing custom nodes extremely easy as opposed to having to go in and manually install them every single time. All you need to do is navigate to this green box here and just click and copy the link. And then what we're going to do is go back to that file structure for the Comfy UI portable that we just downloaded. I'm going to go to the custom nodes folder in there. I'm going to click in my path right here and I'm just going to type in cmd to open up a command prompt for that location.

**3:09** · And then I can just run get clone and paste the link. That's really about it. That's kind of the breadand butter for installing things manually to start.

**3:20** · Again, you can use the Comfy UI manager to be able to look up custom nodes and just click install and then it'll do it for you. But if that fails, just use that manual step for installing most anything. You just navigate to the folder where the model or the node is supposed to go. You find the corresponding GitHub, you get clone into that location. So, let's actually fire up Comfy UI. All we need to do is go back to the main folder structure here and we need to find the run Nvidia GPU.bat. BAT file.

**3:48** · You're going to see a terminal window open up, which is completely normal. That is Comfy UI running. Once it goes through everything it needs to do, it's going to open up in a local host on your browser. And up here in the top right, because we already went through and installed that Comfy UI manager, you should see it here. You can click on it. Check this out. This is a nice little starting point for when you do open up a workflow to be able to find any custom nodes that you may need, install them directly from the manager or to be able to look up any models that you're missing as well.

**4:17** · All right, so once you are within CompuI, the first thing I would recommend is to go over here to the far left and find this template section. And you can browse through some of the popular workflows right here. There are a bunch of other places where you can find workflows. Again, I'll link a bunch of them in the description, but I'm going to point you out to some of the ones that I find the most useful or I recommend for beginners. For video, I would recommend using the LTX 2.3. So, let's go ahead and select this as our very first example.

**4:48** · And you're going to see it's going to let you know that you have missing models for this workflow.

**4:54** · It's also going to show you some tags for what these models essentially are, and that'll help you to kind of map out which folder these should be placed in.

### Models & Custom Nodes

**5:01** · So, you see this one is checkpoint. So, I'm going to click to download. I'm going to navigate to wherever I have Comp UI installed. We're going to go down to the models folder. We're going to find the checkpoints folder right here at the very top. And I'll just click save to start downloading it to that folder. And essentially just repeat the process for the rest of these models that you're going to need. You see you have Laura, um an upscaler model, a text encoder, and another Laura.

**5:23** · So, you kind of want to familiarize yourself with that structure. again, Comfy UI, go to models and then find the corresponding folder right here. So for the Loras, I would put them in the Laura folder right here. So once you have installed those models, you should be able to click here and see the model listed within the drop-down for each of these.

**5:43** · If for some reason you can't find them within the dropdown, that means they are not working correctly, you may need to go double check where they are installed here and then just refresh the page and they should now be available. So once you have everything installed, this is why I recommend LTX 2.3 currently for people just starting out. It is very fast. It is not too taxing on your PC and you're going to get excellent quality even with the ability to prompt audio and even some dialogue. So I'm going to show you a little bit of that.

### Video creation workflow for beginners (LTX)

**6:15** · The workflow is literally just these three nodes. This is technically a node group, which you can see right here.

**6:21** · It's a subgraph. So, we can click in here and you can see everything that is going on underneath the hood. And this is what a standard connection would look like where you're loading in all of your separate models. Uh you're doing your text conditioning, so on and so forth.

**6:34** · I'm not going to dive super deep into this because I know this can look intimidating with all the wires. And I think that this is something that you should kind of just start to piece together on your own, all the functionality of every single little thing over time. So, what I am going to do is just go back and just give you some actionable things that can help you with the process of learning Comfy right now. And the biggest thing I would say is quality of life tips. So, I'm going to point you to some custom nodes here.

**6:59** · The number one being the RG3 custom nodes. You can see them right here where it's showing some of uh the RAM usage, the CPU GPU usage. These are nice, but it's actually not why I like the nodes.

**7:10** · So, let's go to manager. We're going to go to custom nodes manager. And from here, just search for RG3 and go ahead and install that and then refresh once it is ready. And that way, whenever I click play, you're going to see this green progress bar and the node in of itself actually light up. And it's super great just for getting a better understanding of the overall flow. So, if I click into the subgraph, we click play again, you can see how we go through each of these, loading our checkpoint, loading your Laura, going through the text prompt. It gives you a nice extra bit of essential information.

**7:42** · And it's also very nice for troubleshooting. If something does go wrong, this will turn red. You'll see in the top left, the progress bar will also turn lead will also turn red. And you can just click if there is an error and it should snap directly to the node that did fail. So again, highly highly recommended. We're going to stop this for now and we'll go back. Now, the other nodes that I recommend, and this is kind of just personal preference, but I like being able to preview the actual video final result directly in Comfy.

**8:11** · Right now, by default, it is set up to just kind of save to a path. So, it should be in your output folder in Comfy. I want to actually see the video directly within the interface. So, I'm going to use this video combine node.

**8:23** · This is from the Comfy UI video helper suite. So, again, custom notes manager.

**8:28** · Um, video helper right there. Go ahead and install that and then refresh. And those are really the only two essential ones that I use in basically every workflow. So, if you see here, you can't actually take the output of this video and connect it directly to the video combined just to preview it. So, we're going to have to click into the subgraph. And by the way, if you just select any couple of nodes by holding down control and then just dragging like this, if you click this button right here, this will actually convert that into a subgraph if you want to make one of these yourself.

**8:58** · It's kind of like nesting things together. So, we'll pop into here and you're going to see kind of like a group input and a group output if you guys are familiar with Blender. And essentially what we need to do is just take this end images output from the vay decode and just socket that to this output so that we can actually connect that ourselves and you can do that with anything else. So for example maybe you want to also preview the audio connect that to the output and then we'll just pop back to the main workflow here.

**9:28** · Now you can see this image slot and the audio slot which we can use to get rid of the save video.

**9:36** · Bring into the video combine and just connect everything up like that. So now once this is ready it'll play directly here. Terms of general settings this is your frame rate. We'll go 24. Uh for the format you don't want GIF. It'll make all the colors sort of crunched. So we're going to go H.264 MP4. So now we are ready to start generating. I'm going to bump the frames down to 81 here. This is our resolution, which is fine. I think this is our frame rate. Bump that down to 24 just to match. And we can go ahead and prompt.

**10:08** · And I want to see if we can get some of the dialogue to work as well. It can be kind of finicky if you try and give it complex dialogue.

**10:15** · Sometimes it just turns into gibberish.

**10:17** · Uh, but let's see if we can get this dynamic camera movement. Maybe he's jetting through the ocean. We have wind.

**10:23** · We have a lot of different things going on. So I'll say a dapper old man in a speedboat. So I'm going to say this.

**10:31** · Dapper old man in a speedboat across the ocean waves. Windy dynamic camera slight camera shake. And then let's try some dialogue where we can say just like this. The man says the man says subscribe. Now I don't have to ask you guys myself. I can just get this guy to do it for me. And while this is running I'll just give you guys a little bit of an overview of the process. But again I'm not going to dive deep into this. So what it's doing here, and actually this is a good tip. I'm going to stop this for now.

**10:57** · So if you do go into the subgraph, this first text to this first text generate LTX2 prompt is going to take your original prompt that you wrote in and it's going to try and and it's going to alter it a little bit. Uh and sometimes if you are going with dialogue specifically, you might not want that to happen. Anytime you're not using dialogue, go ahead and keep this on because you want to have the clip vision where it's getting a better understanding of your image and it can kind of translate that into terms that it understands better.

**11:27** · But if you do want dialogue and you don't want to alter this in any way, shape or form, you can go ahead and just select this node and click controlB to bypass it.

**11:38** · Again, that's something that I've noticed. Um, it really just depends.

**11:42** · So I'm going to bypass that for now and then we'll rerun.

**11:46** · And right down here it's going through all of the model loaders. So loading in our checkpoint file, all of the Lauras, everything we essentially put into the file structure at the beginning. Right now it is encoding the text. So this is negative prompts as well if you'd like to place in there. So again, I'm not going to overwhelm you with the details, but I'm going to give you the most basic beginner friendly explanation of how the process works of how images and video are created. And again, you don't have to fully have a PhD in how all of this works at the beginning.

### Simplest way to understand how it works

**12:15** · I think learning CompuI is just learning how to get up and running and like hold your own and setting up the workflow, clicking run, and having a successful generation first and then you can dive into the bells and whistles of how to manipulate things to get things the way that you exactly want. So essentially, whenever you hit Q prompt, Comfy UI is creating a blank latent, which is basically just pure random noise like static on an old TV.

**12:40** · Whenever the sampler runs, the sampler is step by step asking the model, given this prompt, given what I know about the images, how do I judge, how do I nudge this noise to be slightly less random.

**12:51** · It does that over and over, maybe 20, 30 times, each step, making the noise look a little bit more like something real.

**12:58** · It's like watching a Polaroid develop in slow motion. It starts as nothing and it slowly resolves into a picture. So once that sampler is finished, you have a vague decode node and that is the translator. It takes the finish latent and it converts them back into actual pixels that you can see and save. So again you add random noise, you add your conditioning like your prompts and your reference images. The sampler refineses it step by step using that information and then the VY decodes that into a real image. That is the short and sweet of it.

**13:29** · So we're already within the final V decode step. Again, on my 5090, this generation did not take long at all. LTX 2.3 is really optimized for running on RTX GPUs. So, let's check out the final result.

**13:42** · Subscribe to Max Novat.

**13:45** · All right, so I do want to show you one more very important step, how to upscale your video. And because again, we're using an Nvidia GPU, we can utilize the Nvidia RTX video super resolution nodes for a very, very easy and great upscale method. If you see, we right click on this. This is 1280 by704. And now we're able to get it up to 2K resolution, which allowed me to even make that clip full screen in the edit, which is nice.

### Upscaling with Nvidia SuperRes Node

**14:13** · So, let me show you how to install this.

**14:15** · All you need to do is go back up to your manager. We're going to go to the custom nodes manager, and we're going to search for Nvidia RTX. And you're going to want to download this one right here where you can see the RTX video super resolution nodes. So go ahead and install the custom nodes directly from here. And to actually get it to show up within Comfy UI, we do need to do one more little step. You just need to Google Nvidia video effects. It should be the very first link right here, the broadcast download resources.

**14:44** · Once you are there, just scroll down and download the video effects or whatever GPU version you have. Again, I'm using a 5090, so I can go ahead and download here and just run through the installation. Once that is complete, there is one last step. You just need to go back to wherever you have Comi installed again, wherever the page where you can see the BAT file. This is where you want to start. Go up to the very top path and then just type in cmd into this path and then click enter.

**15:11** · Once you are here, go ahead and paste in this script, which I'm going to leave in the description. That will install the requirements for you. And then you can just restart Comfy UI and you'll be able to doubleclick and search for RTX and see this video super resolution node right here. Very very simple. You just connect this into the chain where we take our output from LTX. We already set it up. So we don't have this video output. We have the direct image output.

**15:40** · So you're all good to go there. Connect that directly to super resolution.

**15:44** · Change your scale. We'll go quality ultra. So again, super important. You can do quick iterations at a lower resolution here and then actually have final quality that you can bring and post on social media, YouTube, whatever, so that you're not losing anything in the process. All right, so that's the gist of getting started. Keep in mind for each model, usually there's a lot of alternate ways to utilize them. Like for example, if we go to the LTX GitHub, they have some example workflows here for motion tracking and this IC union uh workflow as well.

### Other video workflow mentions

**16:11** · IC union in particular, I'm actually going to quickly show you here. This is essentially additional signals like depth, edges, and pose tracking that you can use for videotovideo control.

**16:23** · Anytime you can control more elements of your generation. I think it's important if you want to try that out yourself.

**16:28** · Again, a link to that workflow will be down below. And you can also check out a separate tutorial I made on Juan Animate if you want a great model for character animation. That model in particular is probably one of my favorites and the one I've used the most over the past couple of months. But I want to backpedal now and talk about some image models and share with you a nice little beginnerfriendly workflow for image creation as well. So in terms of image models, the three big ones are Quen, Zimage, and Flux.

### Image creation workflow for beginners (workflow included)

**16:54** · I'm going to show you my recommended workflow here using Flux Clin. I've only ever used Flux if I need something local. A lot of the time I'm also using API nodes like Google Nana, Banana, so on and so forth because those models are really nice. But either way, this is what I use for local image generation. Flux Klein is an awesome model. It's super super lightweight.

**17:19** · This should be able to run on lower VRAMm GPUs. So, something like a 3090 or a 4070 should be able to handle it no problem. Uh we're using the FP8 distilled models here. So, it's not full size, it's a bit more condensed. And the nice thing about this model, you can do text to image, you can do image editing, and you can do multi-reference generation all in one single unified model. and it is very very fast. So very nice for iteration. So again, this is the workflow that I built here. And you can download this down below.

**17:48** · Just like my other workflows, I like to make everything from left to right where we have our models. You have your prompting up here. All of your sampler settings, which you don't really have to change much here with the CFG. You just want to stay between um 0.9 and 1.1. You can change your steps here if you'd like. if you want to kind of crank it down. I think this might be a bit too much. It's starting to add like too much to the face. And then you can also change around your seed here, keeping the same seed or just randomizing each time.

**18:19** · Super super simple. In terms of the other features, there's also a built-in upscaler. Actually, two different upscalers. Um, this right here is just the normal upscale image using model.

**18:31** · So, you can choose any upscale model that you guys like. The one that I like here is this Ramacri, I think it's called. I also have seed VR2 in here if you want to try that out. This is one of the more popular upscalers. You can bring in the Nvidia super resolution node if you want. I already showed you how to download that earlier. That works with any Nvidia RTX GPU, even down to the 20 series, which is great. So, I can choose whether or not I want to upscale it right after I see my generation. And if you want, you can come over to this fast bypasser and just change anything on or off.

**19:01** · So, if you want no upscaling, you just click and it'll bypass everything for you. So, yeah, not much to say. very beginner friendly. I'm going to show you quickly just an example of the image editing where I say change to this specific black hoodie or black outfit. Uh do not change anything else in the prompt. And I'll show you the comparison view here where you do have that image editing capability. And I'm also going to show you some examples of the style transfer results from video game to photore. And this is really interesting because this is one of the main ways I utilize this workflow in the first place.

**19:32** · I like to bring in low poly 3D renders as my initial reference and then you can bring in any photorealistic reference to try and copy the style of and that way you have control within your 3D model of different camera angles um different environments so on and so forth and you have control over the final output with just your reference image. So very nice for quick iteration uh if you do want to build some 3D into that. And yeah, this is the main one I'm using for image generation. Uh there's also an inpainting workflow.

**20:02** · This is just run-of-the-mill older Flux one, not the new Flux 2. Uh but this is extremely easy to use as well. Uh all you have to do is rightclick, go to open in mask editor. You can draw wherever you want to inp. So I could draw like this.

**20:21** · Click save. And then you just type in your prompt of whatever you want to change or inpaint. Click run. And it's as simple as that. And yeah, that's about it. Other than that, I'm using a lot of nano banana just for video editing, keeping people's likeness intact. It does such a good job at that that we really don't need Lauras like we used to where we're training the model on specific images of a person to retain that likeness. Now we can use Nana Banana to get all these different angles.

**20:47** · Whenever I say API nodes, it's essentially meaning you don't have to go to Runway or Google or whatever specific website to use it. You can connect your API key and be able to use the and be able to use the closed source model directly here within Comfy UI, which is great because you're still going to have to spend credits if you are using a closed source tool like that, but you still have all of what Comfy can do to build upon this and create different workflows on top of the model in of itself.

**21:16** · So, you're not stuck on just that onepage website and just the prompt. You have a lot more options there. If we go back to the templates, I do just want to give a quick little shout at some other things you can do uh like some of these audio presets or even creating 3D models within Comfy UI, which is really cool.

**21:34** · Things like, uh, UV unwrapping and texturing. I know these are still very far behind, but it's cool that we're starting to get some of these different capabilities within a software like this as well. I hope that gives you a nice beginner friendly overview of how you can use this tool. So, as always guys, thank you so much for watching. And thank you so much for supporting and I'll see you in the next

---
title: "Claude Video Editing Just Became Unrecognizable"
source: "https://www.youtube.com/watch?v=Aw3BkmhYu4I"
author:
  - "[[Nate Herk | AI Automation]]"
published: 2026-04-22
created: 2026-05-23
description: "Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=hyperframes-v2All my FREE resources: https://www.skool.com/ai-aut..."
tags:
  - "clippings"
compile_status: compiled
compiled_to:
  - "Wiki/AI视频制作/AI视频剪辑与动态图形工作流.md"
  - "Outputs/SOP与模板/AI视频短剧制作检查清单.md"
remaining_value: medium
---
![](https://www.youtube.com/watch?v=Aw3BkmhYu4I)

## Transcript

### Intro

**0:00** · Claude is now editing my videos end to end. All I have to do is drop in a raw file and it is trimming out the mistakes and the dead space. It's adding motion graphics like you see over here. It's adding dynamic elements like you see over here. It can even add subtitles at the bottom of the screen like you're looking at right here. So, even if you've never coded before or you've never edited videos before, I'm going to show you guys exactly how you can get set up and get outputs that look pretty incredible just like this. All you have to do is use your natural language. It is so insane. Don't want to waste any of your guys' time. So, let's just get straight into the video.

**0:27** · So yeah, I was able to take this, you know, 50-second clip, drop it into Claude, and then it basically cut out all of the mistakes, all of the filler words, and now we have a 27 second clip with all of the motion graphics that you guys just saw. But not only that, you can see we also have this timeline editor, which has all of the actual elements down here, all of the different motion graphics. So if I wanted to, I could delete these, I could move them around, and I could change the timing because obviously what's super important about motion graphics is the timing.

**0:54** · So now we have this actual interface within our Hyperframes dashboard to make some really quick iterations. So today I'm going to show you guys step by step setting up a fresh Cloud project. We're going to get everything we need to get installed installed and by the end you're going to know exactly how to edit videos just like you saw in the intro. All right, so before we get into it, let's talk about the way that this actually works and sort of the tech stack that we're using.

### How the Pipeline Works

**1:16** · So before we were able to use Claude and these other tools to edit videos, this was basically my process. I would have some sort of raw file, which would be a recording, and then I would go in there manually into, you know, like Adobe Premiere Pro and I would trim out all of my mistakes and I would trim out all of the retakes and things like that. And this was all very manual. So, I was doing this manually and I was doing this manually. And then if I wanted to add any animations, I would be doing that manually. And then rendering is not a big deal, but I would be doing that manually as well. And then a few days back, this tool from Hen just dropped called Hyperframes.

**1:46** · And I made a video about how we're able to use Claude with hyperframes to get motion graphics and animations like this. And what I showed you guys in that video was basically us doing these first two pieces manually, but then we were using Hyperframes to actually do the animations and the rendering. So, still a huge productivity boost, but we were still manually doing the trimming and the editing. But now we're taking it a step further because we have this new tool called video use.

**2:13** · and video use is going to be the one that's doing the trimming and editing for us. So, right now what we're doing is we're dropping in a raw file and then it's basically being trimmed, edited, animated, and rendered for us and it's really cool. Now, yes, we could get rid of the manual step of recording the raw file. I don't want to do that for YouTube because I want to keep these videos real, but I did actually make a video about that as well. In this video, I talked about how I used Hey Genen to basically automate me recording the videos. So, I would drop in a script and then it would give us the raw file.

**2:41** · So this step would actually change to a hijen avatar and then because the fact that the hijen avatar is perfect, we basically were able to just remove this trimming and editing step entirely and then we would just get the animations and the rendering done. So there's lots of ways that you can skin the cat here, but today what I'm showing you is basically just manual recording and then the rest from there is taking care of us. And like I said, I'm going to show you guys the step by step. And of course, at the core of all of this, we're using Cloud Code as the orchestrator to connect all these different tools together. Don't be scared by the word Claude Code. I'm going to show you how this works.

### Claude Desktop Setup

**3:12** · It's super simple. So, today I'm going to be showing you guys how to do this with the desktop app of Claude Code. Right here, you can see this is what VS Code looks like, which I've shown in a lot of my previous tutorials. I'm not going to use it today, but that is usually the main way I like to use it. Today, we're going to be using the claw desktop app just because the interface might feel a little less scary. Also, kind of funny, when you search Cloud Desktop app, at least right now, Codeex pops up. But anyways, you're going to install the claw desktop app. You can see you would go to this cloud download page and just download this for your operating system right here. Now, once you open that up, it's obviously going to prompt you to sign in.

**3:42** · And because we're using Cloud Code, you do need to be on a paid plan that has access to Claude Code. So then what you're going to want to do is you're going to choose a folder to work in. So you could come in here, open a folder, and just choose a brand new one.

**3:53** · It can be completely empty, and you'll be all good to get set up. Or what you could do is you could go over to my free school community. The link for that is down in the description. And you could grab this Hyperframe student kit. And all you need to do from here is you need to just grab the URL of this and give it to Cloud Code and say, "Hey, clone this repo. Set up this project for me." just like this. Like I said, link for this is in my free school community. Okay, but let's say you don't do that. What are the other tools you'll need? Well, I'm also going to attach in the description of this video this Hyperframes GitHub repo and the video use GitHub repo. A GitHub repo is basically just a project.

**4:25** · It's a collection of folders and files and Claude is able to look through this and pull in the elements that it needs.

**4:31** · So, literally all you would do is you would copy this link, go into Cloud Desktop, just paste it in, and then I'm going to go grab the other one as well for video use. And I'm going to paste that in. And I would just say, "Hey, I'm setting up this project to be basically my video editing studio. So I want you to look at these two GitHub repos and I want you to pull in the skills and pull in the important information that we need from these so that I could basically give you a raw video file and you would be able to edit it, remove the filler words, and then help me add motion graphics to it." So basically the full pipeline.

**5:01** · And then you just go ahead and shoot that off and let it do its thing. Let it look through those and let it pull in any of the files that it needs. Now, while this is running real quick, you guys might be asking like, why do you prefer to use the desktop app over VS Code or vice versa? Well, typically for me, the reason why I like VS Code is because I can see all of my files. So, this is my Cloud Code project, right? And over here, I can see my assets. I can see my projects. I can see everything that I've dropped into here.

**5:27** · Whereas in the desktop app, you don't have visibility. even though they're working out of the same folder, we just don't have that visibility because on the lefth hand side here, all we are seeing is our other projects that we could switch into. We don't actually get to see all the files. So anyways, you can see it says, "Okay, good news.

**5:42** · Almost all of this is already wired up.

**5:44** · Everything's already set up because my project is already set up. So you guys can either grab the repos or you can just basically do this exact same prompt and it will set up everything for you because all we need is we need the skills from hyperframes and the skills from video use and then we're just going to start building some videos here."

### Trimming the Raw Video

**5:59** · Okay, so because that's already happened, I'm just going to go in here and I'm going to do a slash command, which means I'm just going to clear out this conversation so we can start fresh.

**6:06** · Okay, so I recorded this video right here. It's 50 seconds and it's basically just me kind of blabbing about what we're doing in this video, but I purposely made a few mistakes. I left a lot of, you know, silences and filler words in here. And remember, this is 50 seconds long. So I dropped this into the project right here, and I'm going to ask it to trim it for us. So in here, if I type the at sign, it will show all of the different things that are in this project. And right here, if I go to the bottom, you can see we have edit demo raw, which is that video that I was just talking about. And so now it knows exactly what I'm actually referring to.

**6:37** · And I'm just going to say, "Hey Cloud Code, I would like you to use the video use tool just to edit this video. I want you to analyze it. I want you to remove any filler words or silences or retakes.

**6:49** · And then what we're going to do after that is we're going to use hyperframes to actually add the motion graphics to it. So your first task is just to edit out the mistakes and the filler words.

**6:59** · Okay, cool. So while that's running, let me explain why we're doing it that way.

**7:03** · Because like I showed you guys, ultimately what we're able to do is completely automate this pipeline, but we have to kind of work our way up there. And if we wanted to use video use to basically do everything, it could because within video use, there's actually kind of like a motion graphics skill called reotion, which you guys might have been familiar with already.

### Hyperframes vs Remotion

**7:21** · And the reason why we're using hyperframes over remotion is because we just like it better. I'll show you guys a comparison in just a sec here. But what you could do is say, hey, run the full video use pipeline, trim, animate, and render. I don't want to touch anything. And it would do it. It would do it with Remotion. So, let me show you an example. So, if you guys remember the intro to this video, we had these motion graphics. We had these kind of liquid glass cards, and I thought this looked really, really good. We had this little, you know, animation there. I love this.

**7:47** · This was hyperframes. Now, I dropped in that same raw video that you guys looked at here. I dropped in the same raw one into Cloud Code and I said, "Hey, do the full video use pipeline." And this is what it gave me when it used Remotion.

**8:00** · Claude is now editing my videos end to end. All I have to do is drop in a RAW file and it is trimming out the mistakes and the dead space. It's adding motion graphics like you see over here. It's adding dynamic elements like you see over here. It can even add subtitles at the bottom of the screen like you're looking at right here. So even if you've never coded before or you've never added So you can see it trimmed it just fine because it went from 50 seconds to again about 27. It added things like this. It synced it up to the time that I was actually saying them. So it all felt good. But I just like the hyperframes animations a little bit more.

**8:29** · Real quick, I'll just show you guys a few other examples of what's possible. Here is Remotion. So it has a nice little background. It's got my face in the lower right corner. It has these motion graphics coming in. So, it's not to say that Remotion isn't capable. It's just to say that right now with the new hyperframes, the way that it works with HTML, I just think I like it a little bit more. Here's another example where I changed the background. And once again, we're still able to have animations come in and we can still make things look really, really nice just by using our natural language, which is obviously the big unlock.

**8:56** · But that same style of like animating a course or like a lesson, this is what we got with hyperframes.

**9:03** · \[snorts\] So once again, I think it's just a little bit more sophisticated and it just feels a little bit more engaging. So that's really the main difference between um Remotion and Hyperframes. They don't actually work under the hood the exact same way. So that's important to understand. But as far as like this actual flow, they both basically do this step, which is the animate step, and then they will both go ahead and do the rendering as well. But really, the most important part is that you trim it first and that you have the motion graphics synced up to the exact moments that you're saying the words that you want those animations to pop in at.

**9:33** · So, what's important is that while you're trimming it and then before you animate, you're doing something to get the transcript and have like a timestamp correlated with every single word that you say. And all of that is obviously baked into our pipeline right here. Now, the other thing that I want you guys to think about is the fact that none of this is going to be perfect because it has to get used to your style and the way that you work. I always tell people to think about it like you're teaching a kid to ride a bike. You can't just chuck a kid on a bike and he or she's going to ride it perfectly. You have to hold the handlebars. You have to, you know, make sure that they're balancing properly.

### Teaching Your Style

**10:02** · You have to help them adjust. And over time, it's going to get to the point where that kid is just riding the bike and you don't even have to think about it, but you have to steer it in the right way at first. So, inside of this video use project, there's going to be a few skills. And right here you can see when we were actually doing that thing to just edit it, it used one of its skills called video use and it was just basically doing an edit only for hyperframes handoff. Now within this skill, it has to actually transcribe the video. And there's a few different ways that you can do this. You can use OpenAI for a whisper API.

**10:30** · You can use a local sort of like tool which it can install for you and run in the background. That would be free. Or you could use also 11 Labs API which is what video use likes to default to. Hyperframes likes to default to OpenAI whisper or just whisper. For this video I am using 11 Labs API because I think that it's actually better at finding the right moments to cut. But all three of those methods are just fine. So let's say you did want to use 11 Labs. Okay. What you would do is you would go to 11 Labs.

**10:57** · You would come into the bottom left and click on developers and you would go to your API keys and then you would basically just create a key right here and then copy that value it gives you.

**11:07** · And then you would just need to come into your cloud code project and drop that key into a file called the enenv.

**11:13** · So the way that I would do that is I would basically pull up your project in an actual environment like this and I would create a new file calledv or say hey cloud code create me thev and then I'll go ahead and drop my 11labs API key inside of it. Or if you do want to use uh visual studio code which is like one of the reasons why I like to use it is because I can see everything right here and I could literally just click on my env. This is the example, but I could click on the ENV and then I could just paste in my API key right there. So either way you want to do it, just I typically try to avoid just pasting it straight into the actual chat.

**11:44** · And the reason for that is just because that would stay in the conversation history and just best practice to not do that.

**11:51** · So what you can see is that it comes over here and it says, okay, here's what I've got from the transcript. The raw clip is 50 seconds and there are two clear retake moments to cut. So here's what it wants to keep. Here's the clean intro. Here's what it wants to cut. I have a false start. So, I kind of like started talking and then I paused and then I retake. So, it knows to cut that.

**12:09** · It's going to keep the next take. It's going to cut another section where I stutter and then it's going to keep the end. So, it's going to basically cut it down to about 37 seconds. And then it says, "Okay, I've got two taste calls for you. There's a trailing sew at 4220.

**12:21** · Do you want to leave this as a natural breath or get rid of it?" And then it says, "Cut edges around retakes. I'll snap to word boundaries with 50 millisecond leads." I'm just going to say, "Yep, make this as punchy as possible." And we'll shoot that off and it will come back with a fully edited version for us. And then we'll add the motion graphics.

**12:39** · And by the way, while we're waiting for all this, if you guys do want a bit of a deeper dive as far as like some other methods to edit videos with Claude, and I go into hyperframes a little bit more, I do an even more depth setup and I talk at the end about like some cost and speed stuff, then definitely check out this video after the one that you're watching right now. All right, so that edit is complete. is called edited.mpp4. It is 32 seconds long. And let's go ahead and take a look to make sure that we're all good. Okay. I actually don't know where it put this, so I'm just going to say give me the file path. It gave me the file path right here.

**13:09** · I'm going to copy this and we're going to paste that in to my explorer. And now we have the edited version. Okay. So, this is going to be the example video that we're editing together live in this YouTube tutorial.

**13:22** · So, I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me having to do it. So, what did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file, it will edit it and then it will do reotion graphics.

**13:37** · But, if you don't want to use the remotion graphics, we also talked about how you can use hyperframes for those motion graphics as well. Hopefully now you guys understand. Let's keep on getting this video edited and I hope that you all enjoy this YouTube video.

**13:49** · Perfect. I mean, that was edited exactly the way that I would have done it myself manually. And now we're ready to move on to the next step. And you can see what else it created was the transcript. So, this should have all of the timestamps associated with it as well. You can see here if I go into my video projects and I go into the edit demo and I go into the assets, right here is where we see that edited MP4. And right here, we can also see transcripts. And if we open up this JSON file, we can see the actual transcript, right? We see the full thing, but we also get the wordbyword breakdown. So, we can see that. Okay.

**14:19** · Starts at 1.599 seconds. And if we wanted a motion graphic to start when I say the word you, then we would just need that motion graphic to start at 11 seconds.199. So you can see this is super super precise and that's going to help a ton with the motion graphics. Okay. So how do I like to do this? Well, on the first pass, because we don't yet have a style figured out, we have to sort of steer it like I told you guys earlier. So what I'm going to do is open this file back up and I want to figure out when we want certain elements to pop in. So, here's kind of my process.

### Prompting the Motion Graphics

**14:48** · I'm going to use my voice to text tool, which you guys can see in the description, and I'm just going to start talking and telling it how I wanted to edit this video. Okay.

**14:57** · So, I need you to add motion graphics using hyperframes to this video. I'm going to give you some direction as far as what we're looking for. Okay. So, this is going to be the example video that we're editing together live in this YouTube tutorial. So, okay. So, at the beginning when I say this is the example video that we're editing live together, I want you to pop up a liquid glass style card on the left half of the screen and I want the words to sort of appear as if they are karaoke style words popping in karaoke style um

**15:27** · subtitles and it should look like a title of a video.

**15:32** · I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me having to do it. So, okay.

**15:40** · Okay. And then the next part when I talk about I might make a few mistakes and that's okay. What I want you to do is add a card at the bottom of the screen that says, you know, mistakes will be cut. And then also add a motion graphic on the right side of the screen that just shows like an animation, you know, a visual understanding of what does it mean to edit out and trim mistakes. What did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file. It will edit it and then it will do reotion graphics.

**16:10** · But if you don't Okay. And then the next part when I talk about the video use pipeline of dropping in a raw file and having it be edited and reotion graphics. I want you to animate that. I want you to show me on a liquid glass card an actual animation of raw file being edited up with motion graphics applied.

**16:30** · So just you know show me tell me a story paint a story here with these animations don't want to use the reotion graphics we also talked about how you can use hyperframes for those motion graphics as well hope okay and then the next piece when I talk about using hyperframes instead I want you to um just show a different version of motion graphics maybe a different color or some other different animation style and you can do that as cards both on the lefthand side of the screen and the right hand side of the screen. So that's what we want for this video.

**16:58** · Make sure that everything is syncing up to the exact second where it makes the most sense for that motion graphic or that text to pop in. And yeah, that is your task. Let's see what you can do.

**17:13** · Okay, so we've just shut off that prompt. What I like to do now is I like to switch this to plan mode. So now it's able to basically look at the transcript. It's able to understand our request and it's going to start to plan out. Okay, I'm gonna make this card and here's what it's going to say. Here's what's going to be on it. I'm gonna have this come in at this time stamp. Are you okay with that? And we're basically able to say, "Yes, I like this plan. Go build the motion graphics now." Or we can iterate a little bit before it actually wastes our time and our clawed session limit actually coding out and building the HTML for the video.

**17:45** · So, this planning stage is very important. All right, awesome. So, we got a plan back, which I can go ahead and make a little bit larger here. Okay, so we have our talking head clip. We have the goal to add four hyperframes motion graphics beats which are kind of just like scenes that feel like iOS 26 liquid glass premium UI over a lightly dimmed talking head each synced to the exact spoken phrase blah blah blah that sounds good.

**18:10** · We have an aesthetic direction. We have a motion philosophy doc which if you download this um GitHub repo that I am giving you guys then that will be in there as well. But that just has some best practices that I found for creating these motion graphics. But anyways, we have some color palette stuff. So, beat A is going to be an intro glow with teal. We've got orange. We've got purple. We've got graphite. But now, let's go to the actual timeline. So, this is where we have to potentially make some changes to the plan. There's a bit of a bug here. It looks like this column is getting Oh, okay. Never mind.

**18:40** · I just had to scroll over a little bit.

**18:41** · That does seem like a bit of a bug, but either way, the beat timeline. So, the intro is basically from 0 seconds to 5 seconds, and then we have 5 to 12, 12 to 20, and we have different things going on. So, it's basically showing us what word is the anchor. So, what word is going to trigger the scene to basically start. So, at this point, we would basically go through each of the beats or the scenes to make sure we like what it's saying. So, I'll go through one with you guys. I'm not going to read all of them because I don't want to bore you. But, let's say beat A. And by the way, when I highlight, you can actually leave comments. So, if we need to comment, we can comment on something very specific, which is nice.

**19:11** · But, I'm going to stop highlighting so that stops popping up. We've got a liquid glass card positioned on the left side, fills left half, centered vertically. It covers the empty wall and door area if you guys remember the camera, but it does not cover the speaker, which is great. It's going to have a tiny uppercase eyebrow that says edit demo chapter 1. It's going to have a chrome gradient. It's going to have a large title that says the edit live, and that's going to be on two different lines. And then karaoke run beneath. So, it's going to say this is going to be the example in 34 font. Okay. Timing anchors. Cool.

**19:43** · So, that sounds like it lines up with what I want. I'm going to quickly scan through these other beats and then I'm going to shoot it off.

**19:50** · Actually, I realized there's one more thing that we showed in that intro that I didn't do here. So, let me make a change. I'm going to click on revise and I'm just going to say this all looks good, but I do want to add one more scene at the very end. For most of the video, or pretty much so far the whole video is just my facecam full screen.

**20:09** · But what I want to do is in the last 5 seconds, I want to transition. I want to take the face cam and I want to vertical crop it with rounded edges and a drop shadow and I want to reveal kind of just a dark mode modern looking background and I want the facecam to shift over to the right half of the screen. On the left half of the screen I want there just to be text that says thanks for watching. So now I can just shoot off that revision. It's going to come back with another plan and then I'm going to go ahead and approve it and I'll check in with you guys when we have that first iteration done. But basically that's it.

**20:37** · As you guys saw I was just using my natural language. I was being very very specific. And I know you guys are thinking, "Okay, well, how much time does that really save if you're being that specific every time?" Well, think about it like this. In my real project, I have video projects, right? So, if I open this up, you can see how many different videos I've made. I've made an app release video. I made a hype video.

**20:56** · I made a lesson video. I made an intro.

**20:57** · I made demos. All of these videos are training data. So, let's say I make five different lessons. Now, I can basically say, "Okay, cool. build a lesson design markdown philosophy file, which means every time I build a lesson, just use that. And that's where you truly get to the point of dropping in a raw file and having it edited end to end once you've kind of established a style for that type of video. So like here, you can see I've built three different YouTube shorts. They're not that great.

**21:21** · We're still iterating a little bit, but we're going to get to a point where our shorts automation is so good that all I have to do is drop in a raw video and it will turn it into a short. So that's kind of the mindset that I have here, and that's the mindset you guys should have. And that's why in this example, I wanted to show you guys how specific I had to be to get a good output. Okay, so it looks like we're at a spot where this has come back with a version for us to look at.

### Preview and Iterate

**21:43** · Now, if you come into the top right of the desktop app and you click on preview, you actually can preview it right here, which is kind of a nice feature. And it's just not full screen.

**21:51** · So, so you could definitely do it here if you wanted to, you know, not context switch out, but it's also as simple as just clicking into the tab. But anyways, now we are in here and let's just give this a quick watch and see what we've got. So, this is going to be the example video that we're editing together live in this YouTube tutorial. So, I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me having to do it. So, what did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file, it will edit it and then it will do remotion graphics.

**22:20** · But if you don't want to use the remotion graphics, we also talked about how you can use hyperframes for those motion graphics as well. Hopefully, now you guys understand. Let's keep on getting this video edited and I hope that you all enjoy this YouTube video. Okay, so it's not too bad. Obviously, there's some things we need to fix. Like this was obviously horrible. It didn't get that right. Um the other thing I noticed is that this kind of covers my face a little bit which we'll want to tweak.

**22:45** · And then also um where was it? It oh just in general there's like a grid and I think it's because when they go into this background they want the grid to be there which is fine but having this grid just be there naturally is not what I want. So, at this point, we just have to go back and make some more comments.

**23:01** · Okay, so not bad. All of the motion graphics are coming in at the right time. I think you just made a few mistakes when it comes to the actual visuals. So, the first thing is in beat one, the liquid glass looks good, but it's actually covering my face a little bit. So, if you could just scale this down and then maybe crop off the right side a little bit so it doesn't cover my face, that would be beautiful. The next thing is that across the whole video, there's kind of like a grid pattern overlay that is visible and it shouldn't be there at all.

**23:33** · I like the rest of the beats until we get to the end where you transition into the video crop. So, the problem is you need to crop the left side in and the right side in. So, we keep the center. We keep the face cam and that's a vertical ratio with rounded crop corners.

**23:54** · And that's mainly the issue because right now what you did is you just cropped the right side of the screen. Everything else about the video looks good. So, implement those changes and then we'll give it a look. So, I'll just paste that in and then once again I'm going to shoot this off. Also, I apologize if that video was like insanely loud. For some reason, when it pulled it up in that local host, it just like tripled the decb. So I'm not exactly sure why.

**24:16** · So when we render it, it would be fine, but sometimes in the preview, we get little things like that. But we are lucky that the timing was good cuz iterating on the timing used to be a little bit annoying. But now you can see if I just kind of move this up, we have the audio. Aha. Okay. So this is the actual I believe this is probably the um beat that is associated with sort of like the graph background. Um but we could move these around, right? I don't have to because they all come in at the right times. But this is where the timeline editor is actually huge because you can, you know, shorten things like, you know, we could move this in or out.

**24:46** · We could delete things. And what happens is because we make that change here, that change actually gets reflected in the actual code and then cloud code would see that and just make sure it reflects that change as well. So for quick iterations, that can be a huge timesaver. Okay, so here is the new version. I'm going to open up this local host and let's give it a quick watch.

### Final Render

**25:06** · Hopefully it's not absurdly loud again.

**25:08** · Okay, so this is going to be the example video that we're editing together live in this YouTube tutorial. So, I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me. By the way, maybe I want to play with the spacing because it might look weird with like a right card and this thing at the bottom and nothing on the left. But I really like this this animation. Look at this. Those cards go red and then we have a scissor come across and cut those out. Like remember, I didn't ask it to do that. I just said make an animation that looks like we're editing the video and it did that. Very nice.

**25:39** · Exactly how we edit those out with AI without me having to do it. So, what did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file, it will edit it and then it will do reotion graphics.

**25:52** · But if you don't want to use the remotion graphics, we also talked about how you can use hyperframes for those motion graphics as well. Hopefully now you guys understand. Let's keep on getting this video edited and I hope that you all enjoy. Okay, beautiful. Now that we have that, we could either keep going back and forth and editing like you guys saw or we just basically say, "Hey, give me the render." And then it pops it into your project and you would just be able to, you know, throw that into whatever else you want, upload it.

**26:16** · That's basically it. And like I said, just to switch back to the VS Code version now, because of the way that I've set up this project, every time I drop in raw assets, it all gets organized by project. So, for example, if we look at the edit demo, we now have assets. We have the clips, we have the transcripts, we have anything else that it needs. We have the compositions which are the actual beats HTML. And this is what it's using in order to make those animations display. And this is what we're actually rendering. We have different components. And then we have any final renders in here. And this is where it's verifying the actual screenshots, which is really cool.

**26:47** · I'm basically telling it to take screenshots of what's going on in the scene to make sure that it looks good. Because sometimes it'll just come back and say, "Hey, I've done this, but it doesn't look good at all." So, if we tell it to take screenshots, it has to go verify for itself. And that is just a really nice trick that I found out to do. So, anyways, like I said, now you have all these projects and you can start to make different folders. Every time you want to do an intro, if you want your intros to look like this, now you use this one as a reference and you just make your intros better every single time. And that's where you get to the point where this is like way more automated.

**27:17** · And the other thing I did want to call out is you guys watched me shoot off all of these prompts and you guys saw everything that it built, all of those different HTML files it had to make. How many tokens did this cost? This took us about 238,000 tokens. So, not too bad, but not great either because this will eat some tokens. And that's why the more specific you can be with your planning and with your iterating, the better because you don't want it to go down the wrong path and then it wastes tokens and it wastes your time. So, be specific.

**27:45** · And if you guys want to dive into more stuff, then you can check out this video where I go deeper, like I said earlier, into some other tactics and show off some other examples and how you can get the most out of hyperframes. But anyways, as this slide says, thanks for watching. This is going to do it for today. I noticed that this is a little bit of a blurry thing that I would want to fix, but that would be a super simple iteration for us. But anyways, if you enjoyed the video, please give it a like. It helps me out a ton. And as always, I appreciate you guys making it to the end of the video, and I will see you on the next one. Thanks everyone.

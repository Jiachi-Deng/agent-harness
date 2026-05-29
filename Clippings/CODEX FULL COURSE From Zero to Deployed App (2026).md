---
title: "CODEX FULL COURSE: From Zero to Deployed App (2026)"
source: "https://www.youtube.com/watch?v=hoCWD1aI60Y"
author:
  - "[[David Ondrej]]"
published: 2026-04-11
created: 2026-05-29
description: "Wanna learn how to code with AI? Go here: https://www.skool.com/new-societyFollow me on Instagram - https://www.instagram.com/davidondrej1/Follow me on Twitt..."
tags:
  - "clippings"
  - "Codex"
  - "VibeCoding"
  - "WebCoding"
quality: "must-compile"
compile_status: "compiled"
compiled_to:
  - "Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流.md"
  - "Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环.md"
  - "Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架.md"
  - "Wiki/Vibe Coding/50-SaaS产品模式/API包装型SaaS机会与风险.md"
review_note: "Raw/NotebookLM/2026-05-29--youtube--CODEX FULL COURSE From Zero to Deployed App (2026).md"
remaining_value: "medium"
---
![](https://www.youtube.com/watch?v=hoCWD1aI60Y)

## Transcript

### Introduction: The Power of Codex

**0:00** · This is the ultimate Codex guide for beginners. My name is David Andre and I've spent well over a thousand hours coding with AI. I also used Codex to build Vectal, my AI startup, which got acquired last year for seven figures.

**0:13** · And I'm one of the first people on YouTube to begin teaching Codex. I've helped hundreds of thousands of people learn how to use Codex. So, if they can do it, so can you. Now, to start using Codex, you don't need any coding experience. I'm going to walk you through everything step by step. And by the end of this course, you'll be able to build anything. You will have the skills to turn any idea into a real software application that's fully deployed on the internet in less than an hour. Codex will also make you a lot more productive. And not just in coding, in most areas of life and business.

**0:44** · And I know that because I'm speaking from experience. So here is what we're going to cover. First, the fundamentals.

### Course Roadmap: From Fundamentals to Advanced Deployment

**0:52** · installing Codex, setting up your environment, my personal codec setup, and understanding how it works within IDE. Then we'll build a real app together from scratch and deploy it live so it's available on the internet to your friends, family or potential customers. And we will do all of that just by speaking in plain English to Codex. After that, we'll go into the advanced stuff. Sub agents, skills, automations, git workshries, MCP servers, cloud agents, and more. Yeah, this really is the ultimate Codex guide.

**1:25** · So, let's get into it. Now, there are actually four different ways to use Codex. But the first one I'm going to show you, which is the one that absolutely anybody can use, no matter how bad your computer is, is the Codex CLI. This is the official documentation by OpenAI. I'm going to link it below the video. And luckily, there's a simple oneline install command, right? So if we copy this and open your terminal, which you can do by typing terminal on spotlight search on Mac OS or on Windows, press Windows plus R and type in cmd. So open the terminal, copy this command and paste this in. Boom.

### Setting Up Codex: The One-Liner Installation

**1:56** · This will install Codex CLI on your machine.

**2:01** · And yes, it really is that easy. After that, what we need to do is simply type in the word CEX to launch the Codex CLI.

**2:09** · So first, it shows you that there's update. So obviously we want to use the latest version. So we're going to update. And usually these updates are very fast. There we go. Those 2.4 seconds. So I'm going to type clear again and type Codex again to launch the Codex CLI. Now it will want you to login and we have three different options. If you have CHBD subscription, that is the best, right? It works on Go as well.

### Subscriptions & Plans: Choosing the Right Model

**2:31** · That's like $8 a month, but ideally you would have plus or pro. But again, even the $8 a month subscription works. If you don't have a chair GB subscription, I highly recommend you getting one. It's one of the most efficient ways to spend money in AI. In fact, I think this $20 subscription is probably the single most valuable $20 subscription in all of AI.

**2:53** · Also, you can see that there's a new plan, Pro. Before, the Pro plan costed $200, but now they have two different versions, $100 and $200 a month, just like Cloud Code. You know, OpenAI got inspired by Enthropic. So, if you want a bit more usage than the plus plan, this is the best time in history to begin using Codex because the pro plan now starts at $100 a month. That said, if you don't have any of the plans, you have two more options. Signing up with device code or API key. Now, honestly, device code only works if you have another device that's signed in.

**3:23** · So, really the only two relevant options are signing in with your CI GBD subscription or the API key. Now, since most people already have CHIGD subscription and if you're watching this channel, hopefully you have some form of Chad GBD subscription, I'm going to show you this. So, hit enter and it's going to redirect you to a website where you need to authenticate with the same account you use as in Chad GBD.

### Authenticating Your Account

**3:45** · Now, if you have multiple subscriptions, for example, I have a CH GBD teams account where I have, you know, my team, my people, my employees, and then I have a personal one which I have the $200 a month pro plan. If that's you, then just select the plan which has higher usage. So for me, obviously the pro plan is the highest plan. So I'm going to select that and click continue. Boom. There it is. Sign into COX. We can close this page. So if we open the terminal again, we should be logged in. Sign in with your CHP account. Okay.

**4:14** · So we can hit enter and we should be able to access the CEX agent. There we go. And let me try sending a prompt to see if it works.

**4:25** · Hey, there it is. Who are you? So we are chatting with Codex through the Codex CLI. This is the command line interface and this is like the OpenAI's competitor to CL code. But Codex is without a doubt more powerful at building complex applications, solving deep errors and running for longer without making mistakes than cloud code. So, if you aren't using Codex in 2026, you really are missing out because Cloud Code, while it's good, it's not as powerful as Codex at many of the use cases.

### Exploring the Codex CLI (Command Line Interface)

**4:57** · And by the way, if you're having any troubles with the Codex install if the oneliner doesn't work or, you know, is is throwing some errors, then you might need to check if you have Node.js installed on your system. So, again, I'm going to link this below the video, but this is super simple. Here, you just select the latest version. You you don't have to change that. here. Select your operating system and then run these terminal commands one by one in your terminal. Now to check if you have Node.js, just open the terminal and type in Node-V. And there we go.

### Troubleshooting: Node.js Installation

**5:26** · This is how you know whether NodeJS is installed on your system. If it's not showing any version, then you need to install it.

### Real-World Examples: What You Can Build with Codex

**5:35** · That said, let me show you what I've built for my team and my business with the help of Codex. So, here is one app.

**5:41** · I call it YouTube alpha that we use for titles, thumbnails and analyzing outline videos. As you can see, this is very advanced way to create uh thumbnails.

**5:51** · You upload an image and you can do prompts and based on Nanobana 2 and Nanobana Pro, it generates variations and you can get to a thumbnail like that. Something that inside of Google Studio, it would take you a lot of time because it constantly fails. It can only generate one variation at a time. And we have these different canvases that you can share with other people on the team that allow you to simply create variations of uh different thumbnails.

**6:17** · And this is super efficient and we use it for every single video. And uh it was built largely with Codex. Here's another application that we use for tracking some of our funnels and seeing the metrics. It's integrated with type form and Calendarly. It was built mostly with Codex like probably 90% Codex, 10% cloth code. And this is allowing us to see where the biggest drop off is in our business and what we need to fix. Also known as datadriven decisions.

**6:45** · So stuff like this is absolutely invaluable to me as the CEO. And these are the types of applications that we're able to build in one two three hours and get it fully deployed on the internet with the help of Codex. So if you stick through this entire video, you will have the skills to build app like this for your own life and business. And the obvious advantage of this is that number one, you don't have to pay for other people's software that might be mediocre and not specialized to your use case.

**7:13** · And number two, you can turn any idea you have into a real application in a matter of couple hours. This is the power of Codex. Okay, so let's go back to the terminal. I'm going to type in Codex again to launch it. And the very first thing you need to do is select the AI model. Now, you can see that I already have GBD 5.4 for selected. But if you don't, just make sure to type in /model. Boom. And make sure to select the latest one. Okay? Do not use GPD 5.2. Do not use 5.3 Spark or 5.3 Codex.

### Selecting AI Models & Reasoning Effort Settings

**7:45** · And definitely do not use a mini model. Like, god forbid, please do not use mini models. Use the best model, okay? Which is the latest one, which is GPT 5.4 as of the time of this recording. If you watch this maybe in a month, in in two months, maybe it's GPD 5.5. Whatever is the latest model by OpenAI, you'll see it right here in the description. They tell you what is the latest model. So use the best one. Hit enter. And then you need to select the reasoning effort. How much time does it spend on thinking, right? So there's four options.

**8:15** · Low, medium, high, and extra high. Medium is default. And I would say that's actually a good default because for most things, you don't need it to run for many minutes, right? Low I would suggest you never use. This is simply uh too little reasoning and it will underperform. So I would never use low. Medium is good default especially if you don't want to burn your limits too fast. High is also a great starting point. Most of the time I do have it set to high actually.

**8:43** · And the beauty of high is that if it needs to, it can run for two, three, four minutes if it if the task requires it. But if it's a simple change, it'll just do it in five seconds. Now then we have extra high.

**8:56** · This I would only use for the most complex errors, right? When you when you're struggling with a deep bug that you haven't been able to fix, use extra high. Or if you're doing a massive refactor, like a very risky refactor of your entire back end, use extra high.

**9:11** · But for most things, I think high is the sweet spot and that's what I'm going to select. Now, the way we did it right now, Codex is running on the root of my machine. So, if I tell it where on our MacBook are you running, it's going to run the pwd command and it's going to check where it's running. You can see it's user/david. So, this is the root level of my MacBook, which is not recommended unless you want to do changes like cleaning up your downloads folder or deleting some old applications. Yeah, for these it would be good running it on root level.

### Navigating Directories: Launching Codex in Specific Folders

**9:41** · But if you want to build something like an application, you know, do some AI coding, it's much better to launch it in a specific folder. So what I'm going to do is I'm going to press Ctrl C a few times and this will kill the process.

**9:54** · Right? So again Ctrl C even on Mac OS not command C and this will kill COX process and I'm just going to type clear and then we need to go into a specific folder which means changing the directory cd. This is a very simple terminal command that all of you should learn. Even if you're not a developer there's no disadvantage to knowing this command, right? So CD and you can go for example to documents and if you press tab it's going to prefill the rest of the folder name. Right now if you want to go back up you can do CD dot dot and it goes one level up.

**10:23** · So to go to a specific folder just type in CD and the folders name. But if you want to go back up type in CD dot. Now you might be thinking okay David but what if I don't know all the folders right? We're on the root level. I just open the terminal. I don't know where this is located in my MacBook. First if you want to know where this is located. Type in pwd. This is what Codex did to check where we are.

**10:47** · Let's do clear. But if you want to see what is in this directory, like what are the different files here and folders, you can type in ls and this will list out everything in this directory. So you can see that we have desktop documents downloads. So for a project like this, you probably want to go into documents, right? So you do ls to see everything on this level, all of the folders that are available. And you do cd and you start typing the ones you want to go to. Boom.

**11:13** · And now I'm in documents. Let me type in clear again. LS to list out everything in documents, right? There's a lot, but I know where I want to go to. I'm going to go to CD David.

**11:24** · Boom. David. That's my personal folder for my YouTube channel. And then I'm going to do ls again. Okay. I have a bunch of stuff. So I'm going to go cd into video files. Okay, that's clear.

**11:34** · And then I'm going to CD.

**11:36** · And then I'm going to ls again. And I'm going to CD into the Codex beginner course, which is the video you're watching right now. Now that we're in this specific folder, we can finally launch Codex with restrictions of it being in this folder. I'm going to do that right now. Codex. Now, it will ask you, do you trust the contents of this directory? Right. So, make sure you're on your computer and you trust it. I'm going to hit yes because it's my computer and I trust it. And this is something that you might think, okay, do I need to be using the terminal? You know, is this too advanced?

**12:06** · I literally showed you two commands, ls and cd. ls to list out the files and folders. CD stands for change directory. Go into a specific folder. That's all you need to know because for each project you build, you should be in a separate folder.

**12:21** · Don't be one of these people that like saves everything on the desktop. That's completely amateur and you should avoid that at all cost. Just have a specific folder for each coding project you're going to build and you're good to go.

### Creating the "Agents.md" System Prompt File

**12:32** · Now, the very first thing you want Codex to do, no matter what you're building, is to create agents.mmd file. So, I'm going to say create an agents.mmd file in this project and keep it empty for now. Just put a header.

**12:50** · This is the ultimate system prompt that all of the agents follow. In fact, this is not just for Codex. This is a global convention used by over 60,000 different open source projects. Basically, it's like a readme file for agents. Now, if you use cloud code, you will know the cloud MD file and that's basically the only project that doesn't follow agents.mmd. all the other agents whether that is AM VS Code, Gemini CLI, Cursor, Warp, Kilo Code, Ader, Factory, Codeex,

**13:21** · Rue Code, Windsurf, all the other ones use agents.mmd. And here's what that can look like. It's basically a single markdown file that is a system prompt, right, that the agents should follow.

**13:34** · Now, you might be saying, "Okay, David, but how do I know where to start? Like, I don't have agents.md file." Don't worry, I created a free one for all of you. This is a preset that I use that you can just build up on top of, right?

**13:46** · So, I'm going to link this as a free GitHub gist below the video and you can just copy it, you know, click, you can click raw, get the raw file and just copy control A. Boom. Then you can go into your codeex in the terminal and say like now put in the following text.

**14:03** · Going to wrap it with XML tags like this. This is a pro tip for context engineering. any large paste you're going to do, just wrap it with XML text like this. Boom. Text text and it allows the agent to better see where's the start and where's the end. So, I just literally took the preset from GitHub gist. And as you can see, there needs to be a bit updated like the project name, target user, your skill level, and stuff like that so that it's relevant to your project.

**14:29** · But this is already a very decent agentmd file that's going to make the agent behave better, respond in a more friendly way, and follow best practices. So again, this is going to be linked below the video. It's completely free. Take it and use it. And by the way, if you want to access more presets and resources like this that I use myself for coding and that I use to build vectal and sell it for $1.8 million, make sure to join the new society inside of the classroom. We just released a brand new course, a 3-week outline that's going to take you from a complete beginner to master AI coding.

**15:02** · That includes cloth code, codex, cursor, deployments to versel, superbase, and anything else you need to truly be able to build any type of software with AI.

**15:12** · In these three weeks, you will go from a complete beginner to someone who has the skills to build anything with AI. In fact, let me show you just how the outline looks like. Each week is split into these granular modules between one, three, sometimes four minutes. And these modules are as step by step as it goes, showing you every single step of the setup, all the mistakes to avoid, giving you all the presets, so you can just copy paste them and start using them yourself. And this is designed for people who've never built anything with any coding background, no experience with AI coding agents, nothing.

**15:43** · You will learn absolutely all the things you need to know to not only be able to build any type of software you want, but also deploy it on the internet and start getting users. And in these three weeks, you will have the skill set to do that.

**15:57** · So again, if you're serious about AI and if you want to master AI coding, make sure to join the new society. It's going to be linked below the video. Okay. So the next thing I'm going to show you is image input. You can actually attach images, screenshots directly into the Codex CLI. Now we should start building something right because right now so far we created agents.mmd but we haven't really chosen a project what to build now for apps the woman targeting apps

### Project Build: Designing a Face Transformation App

**16:25** · are insane like it sounds bad but women do spend a lot more money and you can build the dumbest \[ \_\_ \] imaginable and it will work. So this girl got to 300k MR with a manifestation app. I don't even know what that means, but I know what 300K MR means. And what I'm trying to say is that this is the biggest opportunity to build apps is stuff like that's not really obvious to us because each instinct, you know, most of my audience like 98% are men.

**16:55** · The instinct is to build something for yourself. you know, you you want to build a tool that you would use and you go into these highly competitive industries, but there's so much potential building these mobile apps or or it doesn't have to be a mobile app, could be a web app as well, but targeting women and you don't even need to add that much AI. I guarantee you this app is like the simplest thing imaginable architecturally, but it's just branded in a way that works and it clicks and 300K MR something that will be absolutely life-changing to all of us, right?

**17:27** · So we're going to take this approach and actually I have a really good idea which is proven by being in the field let's just put it that way of showing seeing how we would look like.

**17:39** · So AI images are much newer, especially since the rise of Nanobana Pro and Nanobana 2, than AI text, right?

**17:49** · Most people understand AI text. So what we're going to do is we're going to use the untapped potential of AI images to build an app. And this is something that literally every single woman or girl is wondering how she would look like if she had a bit smaller nose or if she had a lip fill or stuff like that, right? And whether this type of stuff should be promoted or not, that's an entirely different conversation. But I think it's a good idea from the technical standpoint because it's going to allow us to use AI images and it's a pretty interesting project to build. Let's put it that way.

**18:16** · So I will say I want to build an app where you can upload an image of yourself and see how you would look like with different facial changes.

**18:33** · Smaller nose, lip filler, foxy eye lift, faceelift, Botox, different skin tone, and at least 10 plus other things that women often do or would like to see how they would look on them before doing anything.

**19:00** · The target audience is women 18 to there's no limit really but let's say 18 to 55 years old.

**19:10** · Update agents.md accordingly and also create readme.md file. This is something you should have in the root of every project is what's called a readme file. This is what displays on GitHub right away. And later in the video I'll also show you how to actually get this on GitHub because that's essential. There we go. Codex has updated it. And now I'm going to do the visual style. So what's another thing that women like is Pinterest. So I'm going to just say that you know whatever this I'm going to copy this. I'm going to shoot a visual input. You can do Ctrl +V. Not command V. Control V.

**19:42** · Command V doesn't work. I don't know why. So just do Ctrl +V to attach this image. And I'm going to say this is what the layout of the app should look like after the user uploads her face.

### Pro Tip: Using Image Input for Better Context

**19:59** · It should generate all kinds of different predefined changes to her face. Again, at least 15 to 20 different images.

**20:14** · Study this layout and save it into both MD files. Okay. So, this is how image input looks like. You can literally take a screenshot of something maybe of a website you like some style you want to copy even an error or the layout you don't want to you don't like the layout of your current site take an image and attach it with your prompt. This is something that so many people are underutilizing. The ability to attach an image input is very very OP.

**20:37** · And by the way if you don't know how to take a full screenshot here is how on Mac OS command shift and free takes a screenshot of the whole screen. So you can just copy and paste it into an AI chatbot or into Codex itself. On Windows it's print screen key. You should have a dedicated key for that or win plus print screen.

**21:00** · And on Linux it's print screen as well.

**21:02** · So this is how you take screenshots. And when I code with AI, I attach screenshots all the time. Like every other prompt includes at least one attached image. It really is underrated thing that beginners are not doing. Now another thing I'm going to show you is web search. This is one of the built-in tools into Codex, but again, very underutilized. So, I'm going to say use the web search tool to find the 20 plus most common facial cosmetic surgeries women do and save them into a single bullet list into readme.md file. Boom.

### Using the Web Search Tool for Research

**21:39** · So, now Codex will browse the web, right? It has a lot of knowledge built in because the model has a lot of it baked into the training data. But for stuff like this or maybe you want to check the latest documentation, maybe you are using like a obscure framework and you want to make sure that you are using the correct docs then tell it to do web search right it can it's not going to be a deep research but the web search here is pretty solid like opens web search is on the level of normal complexity search I would say. So this is another thing is like telling it to do web search to find more information.

**22:14** · Don't just rely on it with the training data. It knows a lot in the training data, but for stuff that's up to date, it can do customer research. This is actually less of a coding, more of a marketing. I'm learning more about that my target avatar for this build project to make the app better, right? And this is something you can do when writing a landing page, when writing email copy.

**22:33** · Use these AI agents to understand the industry more, to understand your users more, to write better copy, to do competitor research. There's so much you can do with tools like Codex. People think it's only for coding because it's in the name Codex, but it's not. You can absolutely use it for marketing, for hiring, for growing your business in all kinds of various ways, for managing your personal productivity. There's literally an endless ways you can use Codex.

**22:59** · Anything that you as a human can do on a computer, you can use AI agents like Codex to help you save time or even do it fully autonomously. Okay, so there it is. It spent a solid minute and now it uh created the list.

**23:17** · I would say uh I did not tell you to remove any of the things we already had just to add to it.

**23:27** · So please do not remove the stuff I told you earlier.

**23:32** · Aka different facial changes. Okay. So here Codex did multiple different web searches until it had enough info and then it saved the results into our files that is much more accurate than what I could think you know women want to see on their face. This is based on multiple web searches. So I'm going to trust that a lot more. Okay. Let me show you another cool feature inside of Codex.

**23:52** · Let's say you accidentally shut it off or maybe you don't use the computer for a few days and then you want to go back to previous session but you start Codeex and it's a new session, right? Every time it creates a new session. Well, guess what? There's a command slash resume where you can resume a saved chat. And here it is. We can see that we have this one chat here and hit enter.

**24:10** · And this is the chat that we were just in with the web search and with uh yeah, with the app idea that we're building right here. So, anytime you want to go to a previous conversation, just type in slash resume. Now I'm going to ask it suggest 10 potential clear names for this app idea.

**24:26** · Let's see what Codex cooks up here.

**24:28** · Beauty. I like beauty. I like number two. Let's go with that. Okay. Amazing.

**24:33** · So it updated all the references to use this new name. And by the way, not every time is it good to resume a previous session. Sometimes if there's a lot of like irrelevant information, a lot of noise, it's better to start with a fresh session, which by the way, you can also do by typing new or clear. Both of these will start a new chat. You don't have to crash the terminal and start Codex from scratch. Type in slash new or slashcle and that will completely clear everything and begin a new Codex session.

### One-Shotting an MVP: Designing the Web App

**25:00** · Now, what I'm going to do is I'm going to show you just how powerful Codex is by telling it to oneshot this whole app. So, ideally, this would probably be a mobile app, but I'm recording this on a computer, so I'm going to show you a web app. So, I'm going to say, let's build this MVP as a web app.

**25:17** · Ask me four concise questions to understand my vision for this based on what's missing in and then tagging files you do to add symbol and then you read me or agents IMD I mean these are the only two files we have right now in this project but tagging files is essential because it tells the agent look there look into this file

**25:42** · this is essential context and then I'm going to say be concise because um context has a tendency to be very verbose, you know, and like yap a lot.

**25:52** · Okay. So, do you want the MVP to use real AI images generation editing? So, I'm going to use voice prompts.

**26:00** · Yes, I want the MVP to use real AI image editing. We will use the nano banana 2 model from open router API. In fact, I'm going to give it the exact model slug.

**26:12** · So, there we are. Nano banana 2. Here we are. Here is the exact mortal slug.

**26:23** · Save it.

**26:27** · I think the first version doesn't need to have any accounts.

**26:30** · It should just be upload only. Question number three, we should store this in local storage for now. Question number four, what matters for V1 is all three of these things. Realistic results, fast generation speeds, and beautiful gallery style experience. We will get fast generation speeds if you use the exact models like I gave you above. And the realistic results just means that the prompts we include cannot be too aggressive.

**26:59** · And the beautiful gallery style experience, we need to copy the interface and the layout of Pinterest which I sent you earlier. Now save my answers into both MD files.

**27:12** · Okay, so now I think I've given enough context. So next I'm going to launch it and I'm going to switch to extra high and I'm going to try to have it on oneot the entire app. I'm adding your MVP decisions to both dogs. Real AI editing.

**27:25** · Okay. And actually I'm going to show you one more pro tip. This one is super valuable is how to double the speed of codeex. You can literally make it faster and that is with a single command slashf fast. Okay, so it finished typing. So if you type in /fast, you can toggle on fast mode. Now obviously this will burn through your limits sooner. So if you only have um Go the $8 subscription or the $20 subscription plus, you will uh burn through your limits fast.

### Doubling Speed with "Fast Mode"

**27:54** · But if you have either the $100 a month pro plan or the $200 a month pro plan, which is what I have, then just always be on fast mode. There is no reason not to be on fast mode. It's very good. It just doubles your inference speed. So, it's absolutely addictive.

**28:09** · And I'm actually going to do /model before I deploy it. I'm going to select to extra high. Actually, no, I think high can handle this. Never mind. I'm going to state on high. I'm going to make sure I'm in fast mode. You can see it also right here at the bottom. I'm going to say now get to work and build this entire app fully and completely like a professional developer would.

**28:28** · Again, make it a web app and keep building until the full app has been finished.

**28:36** · A very simple prompt in plain English and I'm just going to have Codex get started on this and build a whole app for us hopefully in one shot.

### Setting Up an IDE: Installing Cursor

**28:44** · Now, while this is going, I'm going to explain to you how to use Codex with your own IDE. IDE stands for integrated development environment. And this is what you need when you're building software. Now, obviously, for simple stuff, for a simple demo, you can just stay in a terminal like this and have the agent do everything. But the more advanced, the more complex your software gets, the more need for a proper ID. You can see the code, you can see your file structure, you can use Git easily, you have integrated terminals. There's many benefits of using an IDE, and there is no reason to be scared of it.

**29:15** · It's just like any other app. So, if you're able to install Slack or Microsoft Teams or a video game on your computer, you can absolutely install and set up an IDE.

**29:26** · It's that simple. Now, if you don't know what an IDE is, as I said, it stands for integrated development environment. And a simple explanation is that's a software application that combines essential developer tools into a single interface. So, this is a great article from GitHub. You can read it. But basically, IDEs have code editors, debuggers, compilers, version control systems, and AI capabilities. But the beauty of Codex is that it can do most of these things for us, right? So we're not going to be debugging or compiling or doing the version control.

**29:56** · Codex can do these things, but you still want an IDE to see the code and to understand it. Now, by far the most popular ID in the world is Visual Studio Code, also known as VS Code. And this is a great IDE because not only is it open source, it's also completely free. And u everything is built on top of it, right?

**30:18** · So if you use windsurf, anti-gravity, cursor, all of them are built on top of VS code. So if you start using any of these idees, it's very easy to understand other ones because they are all forks of VS code. In fact, you can literally go to the VS code GitHub and you can see it has 184,000 stars and this is the official repository by Microsoft. So they are the inventors, creators of VS Code, but this is one of the most popular open source projects of all time.

**30:47** · And if you have an brilliant idea for a unique AI vibe coding tool, you can just fork it. You can see there is many many forks of VS Code and that's because it's not only really really good but also very easy to use. Now my favorite fork of VS Code is actually cursor. This AI powered IDE that right now they have some features that VS Code doesn't have but uh yeah I've been using Cursor for like two years over two years now and it's very easy to use and you can also get started for free.

**31:15** · You don't even need to pay for any of these subscriptions because we will be running codecs inside of Cursor. And they actually complement each other very nicely. So I'm going to click on download for Mac OS. And by the way, just go to cursor.com to download it.

**31:29** · And by clicking this button, it will begin downloading the cursor installer.

**31:33** · Boom, there it is. So double click on the installer and simply drag in cursor into your applications file. Then you can just type in spotlight search and type in cursor which will launch the cursor app. Now, if you're doing this for the first time, it might want you to log in and create a cursor account. But again, you can do that completely for free on their website. So, just do that.

**31:53** · And then you'll see a screen like this where it's telling you to open a project, right? So, I can open project.

**31:59** · And actually, I'm going to open this same project right here. Codex beginners course. Uhuh. I'm going to open this.

**32:06** · And this is now we can see, you know, on the right. By default, it's on the left.

**32:11** · So, by default, you're going to have it like this. Okay.

**32:15** · Boom. This is what it's going to look like for you by default. In the left, you have the files. In the middle, you can open any of these files and see the actual contents. And on the right, you have the cursor agent. As you can see, I have Codex here set up, but I'm not going to get too ahead of ourselves.

**32:29** · Right. So, this is the layout, but personally, I prefer to have this on the right. So, you can just right click in the header of the sidebar and click move primary sidebar to the right. So don't be confused when the sides are swapped.

**32:41** · This is how I prefer to have it. But you can already start to see the benefits of having an IDE. Not only do we see the actual codebase that we're building, we can see the structure of it and what folders we have, but also you can click on any of these files and you can see the code for yourself or maybe see the prompt, right? Agents.md see the prompt and you can change the system prompt easily. And if you do command I, you can close the AI sidebar to have a full vision. If you do command B, you can close the primary sidebar. But there is many benefits of using an IDE. But one of the main ones in the era of AI coding is the integrated terminal.

**33:13** · To start out, just do command J or control J on Windows. And this will open the terminal inside of cursor or VS code. Again, all of this is literally the same for VS code or wind surf or anti-gravity. All of these things will be the same. So if you learn the basics of VS code, it's so easy to switch between these different IDEs.

**33:34** · Now here what we can do is actually we can type in codeex and launch codex in this project right and then here if you drag in on the node and drag it to the top we can have it in the main window so we can run multiple codexes inside of cursor and this is

**33:52** · both better for AI because again anytime you launch the integrated terminal it's already in the correct folder you don't have to do cd and ls and navigate into the right folder it's already in the correct folder so any agent we launch, it's going to be working on this project. It knows that we're working on this project. But another benefit is that for you as a human, you see everything and you can easily manage agents and you don't have to, you know, wonder what they're creating and what files you have and don't have. It's much better for everybody involved basically.

**34:22** · So, let's switch to the terminal and let's see what's happening.

**34:26** · It wants to allow installing. Okay. So, I'm going to do yes.

**34:30** · In fact, I'm going to put you on more of a tip, more of a game. How to launch Codex so you don't have to do these constant approvals. And that is by putting it in YOLO mode. So, if you type in Codex, you can do space dash yolo.

### Running Codex in "YOLO Mode" for Permissions

**34:43** · This starts it with full permissions.

**34:45** · It's like dangerously skip permissions for cloud code, right? If you're familiar with that command, cloud code, dangerously skip permissions. This is the same command but for Codex. So, I'm going to drag it up and we're going to be using Codex here. I can kill this process and let's see what's happening in this terminal. The app builds verification pass two issues current tool. Okay, so the llinter found some issues. So it's fixing them by itself. So it seems like it built a full app in one shot. Look at this.

**35:15** · Hundreds and hundreds of lines of code without me having to intervene or guide it or anything. This is the power of Codex. It is the most persistent AI agent that can run for longest and it makes the least mistakes. So I'm not joking when I say people who don't use codeex are missing out because it really is essential for building software.

**35:35** · Okay. So now it's fixing some of these issues and we should be able to start the app. So I'm going to say study the code base and tell me how I can start this app. Again with AI you can be as stupid sounding as possible. No prompt is too dumb. The worst thing you can do is not send a prompt and not ask. Right? So it's going to analyze the codebase. It's going to see what text tag we have and see okay this is the next JS project. So we need to do npm rundef.

**36:03** · Can the app start even without the envir let's ask that question. Yes the app can start. Okay let's see if the terminal is running here. It build the beauty mirror like it ran for like 8 minutes or something. The app is okay. Is the front end actually what I'm going to do is I'm going to kill the terminal here. I'm going to resume the same codeex but inside of cursor inside of the IDE. So again press command J to launch the integrated terminal and I'm just going to do arrow up.

**36:34** · This is by the way a pro tip. If you do arrow up it goes through the latest the terminal commands that you already typed in. So you don't have to type in the same stuff over and over.

**36:45** · I'm going to do d- yolo again. Boom.

**36:48** · Drag it up again all the way to the left. And actually for your convenience you can rename it. So you can do like rename codex 01. Boom. Let's go here.

**36:57** · You can right click, rename codex 02.

**37:04** · And here I can do / resume to resume the chat that we did earlier.

**37:10** · Here we go. And now we have our own chat which we were running in the Mac OS dedicated terminal, you know, like this.

**37:16** · But now we're running it inside of the IDE. So it's uh all in one place. It's way way more convenient, way better.

**37:24** · So, I'm going to say uh is the front end running? Ask a super blunt question checking whether it's running.

**37:34** · It gave us these steps, but it should be able to do all of these steps by itself.

**37:40** · No, nothing is listening. Okay.

**37:44** · So, I'm going to say start locally. I'm going to copy this whole thing.

**37:50** · There we go. I'm going to copy that. I'm going to say please do these steps yourself. Steps.

**37:58** · Boom. Steps. I'm going to wrap it up with the XML tags. Most of these it should be able to do itself.

**38:05** · U except for the open router API key.

**38:07** · We're going to do that in a moment. But I wanted to launch the app to see what it looks like. Okay, so it created an inv key and let's see if I can start the server. I'm actually going to start myself npm rundev go local 3000. There we go. This is not bad at all. Wow. Okay, so in the next section we're going to add open router and we're going to actually start testing this. Okay, so the app is running and we can upload a file. This works nicely.

### Using the Codex VS Code Extension

**38:34** · However, before I add the opener API key, I want to show you one more thing and that is another way to use codeex inside of an IDE and that is the IDE extension. So, inside of VS Code and most other IDEs, you will see this button right here. This is the extensions button. When you go here and type in Codex, you'll go to the marketplace and you will find the OpenAI codeex extension.

**38:59** · It should have over 3 million installs and make sure to install it, right? So it's completely free and it works the same way. You can use the same account and this is another way to use Codex.

**39:11** · Now you might be thinking okay David but why do we need this? Why are we like why are you showing me the extension when we already have the CLI? Well inside of cursor if you press command I or control I on uh Windows you'll see the primary agent sidebar or the secondary sidebar whatever you should see button at the top once you install the extension. Make sure to click enable. Right? If you don't see it, you should click these three dots or these three dots and click open C codeex sidebar. So this is this right now.

**39:40** · Here we can use CEX just the same way but with a nicer user interface. So if you prefer to use CI GBD and you kind of don't like the CLI, you know, which a lot of people don't like the terminal interface because, you know, it's not as beginner friendly, then the extension will probably be more for you. In fact, the extension is my favorite way to use Codex. And again, there's four different ways to use this.

**40:07** · And I'm going to show you the other two.

**40:08** · So far, I've only seen two ways to use Codex. The CLI command line interface and the extension. But I'm going to show you more two more later in the video. So here, you can use Codex the same, right?

**40:18** · We have the models right here. Select the model, select the reasoning effort, and you can type in /fast to turn off or turn on fast mode. Obviously, I do want to turn it on. So this is how we can use it with uh two agents at once, you know, one running in the CLI and one running in the extension.

**40:37** · So let's add the open router API key.

**40:40** · That way um the app actually works. So what remains just adding the open router API key. Yes, we're local.

**40:53** · Okay, there we go. All right, so we need to do that. So, let's go to open router.ai.

**40:59** · Click on top right. Make sure to create an account if you don't have one. Again, you can get started completely for free.

**41:04** · Then, when it comes to credits, charge up couple dollars. You don't need $300 or like I have. Just $5, $10 is enough.

**41:12** · And the beauty of open router is that you can use any model you want, right?

**41:16** · So, let's say a new model drops. Okay, we have entropic opus 41.6 fast. That is crazy. I didn't know that's, you know, open router. Well, we can use this or we can use GLM 5.1 which is one of the best open source models right now or maybe the latest version of Gemini 3.1 Pro or if you want GPD models, GBD 5.4. The point is Open Router has all of the models. So, you only need a single API key for your app to work with everything. Now, we specifically want to use Nano Banana 2.

### Integrating Google’s Nano Banana 2 Model

**41:45** · This is uh Google's fastest image editing model and it's much cheaper than Nanobana Pro and much faster than Nanobana Pro. So this is the official name Gemini 3.1 flash image preview but it's also popularly known as Nanobana 2. So again, create an account.

**42:04** · Go to top top right on the settings.

**42:06** · Click on settings. On the left, click on API keys. And then click this blue create button in the top right. You can name it something like a beauty mirror API key. You know, it's the name of our app. Let's put some limit like $20. This is good practice. Always put a limit. If you use something more, then just put like a weekly limit, you know, if you don't want it to run out. But definitely put a limit on every API key. It's good practice. then create and never share your API keys with anyone. Okay, it's like passwords. Keep them private.

**42:35** · I'm going to rotate my API key before uploading this video. But for now, I'm going to copy switch back into cursor and we need to put this in the env.

**42:48** · So, uh, env.

**42:51** · Okay, I'm just going to send it to agent. This is not the best practice.

**42:54** · Here's the API key. Create the env file.

**42:59** · This is definitely not best security practice, but it is the simplest. I'm just going to send it to agent and he's going to replace it in the env.lo, which we should be able to find if we close some of these things. Yeah, there it is.

**43:12** · Yeah. So, this is why you also should u use an IDE because you can actually access these files. Also, I'm also going to say create a detailed git ignore for this project because we are getting to the point where this makes sense. uh to throw this up on GitHub and we should actually initialize a G repository even before uploading this to GitHub which we can use our extension for start a new Git repo in this project and do the first commit. Boom. The agents already know what Git is.

**43:44** · They know how to work with it and um yeah they know they know what to do and you can use Git even without GitHub. So even when you're building a project locally and you're like, okay, this, you know, I don't know if this is going to continue. I don't know if it's worth throwing up on GitHub, you should still use Git, right?

### Version Control: Git & GitHub Integration

**44:02** · So Git and GitHub are not the same thing. They're not the from the same company. Git is a open source thing, open source project that is built for version tracking. It's created by LOS, the same guy who created Linux, and you can absolutely use it locally. It's for version control. You should use it in any project. In fact, I should have created the Git repo way sooner. There's no point to wait. Even if you don't plan uploading it and pushing it to GitHub, you should absolutely use Git for every project. Anyways, uh let's I guess reload and let's see if this works.

**44:32** · So, what I'm going to do because I don't want to disrespect anybody, I'm going to take a AI girl New York. Okay. So, I'm going to zoom in a lot. I'm going to screenshot her face because that's what our app does. Save it into downloads.

**44:53** · Save to documents. There we go. And then let's go back to our app. Let's reload this. And let's choose a selfie here.

**45:02** · There we go. So the image is on the left. And uh we can select. Okay, these are already all selected. Okay, let's click on generate beauty mirror. Let's see how this look with fuller lips.

**45:17** · Smile line softening. Okay, generation failed. We're getting a bunch of failures. So, I'm going to screenshot this. Actually, great. I'm glad it didn't work on the first try. I'm going to screenshot this. Copy to clipboard.

**45:26** · Back to cursor. And I'm going to paste this in. And by the way, you can also paste in into the uh extension. It looks better. But, uh I'm going to paste it into the same codeex because um it has all the context. Or wait, was it this one? Which one was the builder one?

**45:45** · Okay. Yeah, this one. 01. That's the builder one. I'm going to paste this in and say investigate why I'm getting this error and fix it.

**45:56** · So obviously we can also open the console with F12 or command option I and see if there's any errors here. There are not. We can close that.

**46:08** · Uh um maybe we can look into the terminal. I don't know. The terminal is running in this guy I think. Okay. Yeah.

**46:17** · One background terminal running. So I should have probably sent it to the same uh same agent because this one is seeing the outputs of terminal. Do you see any errors in the terminal logs?

### Advanced Debugging & Prompt Engineering Techniques

**46:35** · But right now I'm not debugging in the best way because I'm running checking the current dead server directly. If there any runtime errors they should show there what I see.

**46:48** · H maybe we can reload. No generation failed. Everything is getting generation failed.

**46:55** · Okay. I'm going to let this agent run.

**47:02** · Okay. Actually this is good. So to debug this, I would use perplexity deep research.

**47:09** · Research the proper way to use nano banana 2 model inside of open router.

**47:13** · And then I'm going to give it the exact slug model slug. Right? So nano banana 2. Here we go.

**47:21** · This exact model. Boom.

**47:24** · And how to properly attach images to it and send text prompts. Check the official documentation and give me a detailed report as a single markdown file.

**47:34** · So probably what happened is um Codex messed up the open router formatting. So I'm going to do a deep research and you can use CH GBD research. You can use Gemini DB research doesn't matter. I think perplexity has the right balance of depth and u quickness. So I'm going to use this to figure out what's happening. This Codex is running. It's doing some web search itself. But again web search is not deep research, right?

**48:00** · This is good for a quick info but not a docs. So actually I'm going to say do we have a good place to store different docs or not? I would probably create a /doc folder. Okay. So I'm going to say I'm going to switch to model and medium.

**48:21** · Create slashdocs folder on the root level.

**48:26** · And in there create open router nano banana to syntax.mmd.

**48:36** · Keep the file empty for now. Just add header.

**48:41** · And I'm going to put in the output of the deep research in there. And I'm switching to medium because u most changes don't require high. And now what we can do is do we can do command P or control P on Windows to look up this specific file. Right? So I can do nano.

**48:56** · Boom. Here we go. Open our run two. And we can open it directly. This is the beauty of an ID. You can open these files directly and paste stuff in.

**49:02** · Right? So we don't have to interact with the agent every time because perplexity here is going to give me the results of a deep research. And I just want to paste the results into the file, not have the agent rewrite them. Okay. So it's creating the markdown file. Here it is.

**49:16** · We can click on download. Download as markdown.

**49:20** · Boom.

**49:22** · Actually open that. Double click. It's going to open in some text editor. It chose anti-gravity for me. It doesn't matter. Can even use notepad. But I'm going to copy the contents. I'm going to replace this here. Now I'm going to say read. I'm going to tag the file. Open it. Now there it is. I'm going say and analyze our codebase to see what is different and fix it.

**49:48** · So this contains 520 lines of official documentation from open router on how to use this specific model and how to attach images and uh yeah now I'm just going to dispatch codeex to fix it right so this is one of the essential prompt engineering techniques is providing enough context another thing about prompt engineering especially for AI agents like codex is clarity you need to be clear in what you want a lot of you are being too vague

**50:17** · now you don't like the mid mid with curve right okay this meme I want to show you this meme because it's exactly applicable to prompt engineering the people here the complete beginners complete dummies they are too vague their prompts are too short and they don't tell the AI agent enough the agent doesn't know what the user aka you is trying to do agent is confused in the middle the people around 100 IQ they are like spending five minutes on every single prompt they use like some advanced templates prompting templates, you know, they have everything prepared.

**50:51** · They're using like 10 different things.

**50:53** · They're copying prompts. They're purchasing prompts from others, doing crazy stuff, right? The people at 100 for the IQ, the best people at prompting, they write concise prompts, but they're super clear. They're very clear in terms of what they want, what they want the agent to do. And they don't spend 10 minutes writing a prompt.

**51:11** · They just build, they just build and refine over time and just send it. So, this is absolutely applicable to pro engineering. So obviously you don't want to be at the beginning where like your prompts are confusing and the agent doesn't even know what you want, but you also don't want to be in the middle where you're like spamming the agent with unnecessary information and the prompts are too long and too confusing and everybody is confused, right? And you're just taking 15 minutes writing every single prompt. So this remember this because it's applicable to prompt engineering.

**51:39** · Now another thing is like once you have git established you can just tell Codeex to push you know. So like I don't have GitHub connected but I can say stage all changes and do a get commit. Boom. And it will check what changed and it will fix it and will do the commit for us. You don't even have to write your own commits now because AI can do get status. It can look into the files to see what changed and then it can just do the commit yourself allowing you to do comets a lot more frequently.

**52:06** · And that's another mistake people make when they get into AI coding is they don't do enough comets. You should be doing a commit every 10 to 15 minutes on average. I'm certain of that. So, what is happening here though?

**52:20** · Uh, let's try again.

**52:24** · Reload our app.

**52:28** · We're going to clear session.

**52:30** · Choose the girl again.

**52:33** · Boom. Attach.

**52:36** · And let's generate. Let's see if this works or if we get failures again.

**52:44** · All generations failed. Provider returned error.

**52:51** · Okay, it's making changes. So what I'm going to do is I'm going to start here with high read open router.

**53:00** · Boom. And analyze the error we are getting on the screenshot.

**53:08** · Yeah, let's see. Wait, it it's I'm going to say kill the whatever is running on local host 3000 and start our front end again.

**53:21** · You might need to reset hard reset the server. Okay, so our front end is running. Let's reload. It's suspicious that all of these are taking same. Make sure that our app does all of the different API calls. open router in parallel totally disconnected from one another. That way if one fails the others are not affected.

**53:53** · It's crazy. It should not be taking that long.

**53:59** · and make sure we are using this exact model and following the official docs in open router. Boom.

**54:12** · Get to work and implement the necessary fixes.

**54:17** · Boom. We're going to have this running because uh Oh, wait. It works. Never mind. I'm going to stop it. Uh, okay.

**54:24** · There's a massive massive issue, though.

**54:26** · It's waiting for all of them to be finished.

**54:28** · But it works. Look at this. So smaller nose. Uh we should have like the original image displayed.

**54:36** · But this is like a Pinterest layout.

**54:38** · This is already really solid front end by the way. Brighter skin tone, chin refinement.

**54:44** · Yeah. Fuller lips. Definitely this works. Smile line softening. This is really nice. Okay. So we managed to fix the error. I'm not sure what it is. What was it? because codex exit. So I'm just going to say stage all files and do a get commit. Actually this is how I like to work as well having one agent on the left which serves as a advisor of sorts and then these codex u you know agents here they can be on high or extra high.

**55:16** · So let's switch this one back to high and this one is usually on medium and just answers changes and it sort of more like adviser. you are going to be my advisor. Now, even better than this because both are same model, right? Both are GPD 5.4. This is already really good using CEX in the extension here on the left and then having the these powerful codexes in the CLI on high or extra high solving the problems and running, you know, for 20 minutes straight.

**55:44** · However, if we want even more power and even more variety, we can use the built-in agent in cursor. So remember we are using the codex extension but cursor has his has their own agent right. So in the chat you can click here you can select different models. So you click add models going to take you to cursor settings and you can enable like opus 4.6. There it is. And then we can select it here or maybe Gemini 3.0 pro maybe composer 2. That's model from cursor.

**56:14** · But the beauty of this is that you can use a different model. It says fast mode expensive.

**56:19** · Using fast mode is six times more expensive than regular mode. That is pretty crazy. But whatever the point is that like you can chat with different models. So Opus 4.6 currently is the best available infropic model because they have the mythos which they didn't release. But I can say like explain the structure of this code base and the text tag we are using in simple and plain English. Enthropic models are much better at talking, at explaining things, at being conversational.

**56:49** · So this is much better model for being advisor. I say like remember to be a lot more concise with your responses. Save this into memory. So this is how I prefer to work at least one opus 4.6 and then GBD 5.4 agents for advanced tasks, right? And the benefit of this is that on some things Opus is going to be better. On others, GPD 5.4 is going to be better.

**57:16** · So this is another reason why you should install cursor as your IDE is because of the built-in agent that allows you to use all models. So cursor is like the open route version of IDE. They have no bias.

**57:29** · They let you use OpenAI models, Gemini models, XAI models, enthropic models.

**57:34** · They don't care. So you know you you can have opus here and use it more like a like a asker like a consultant and understanding the changes right so like explain the last three comets to this git repo study them and explain in simple terms how they fixed the issue we were facing because I want to know you know how was this fixed and this is how you reduce technical debt technical debt is a term when you're building something faster than understanding it. So let's see.

**58:06** · Okay, this is too long to say make your answer simpler and shorter. Boom.

**58:14** · Initial commit created. The app was showing useless generic errors. Fix digs into the nested API response to find real error messages. Bomb image quality from 0.5K to 1K. Close the models text explanation when no image is returned.

**58:27** · Okay, so I'm actually going to start another um task here. I will say refactor the way our app works. so that the resulting images from open router are shown one at a time, not all at once. Right now, the app waits until it receives the slowest generation until it shows everything.

**58:56** · Also, I want the API calls to be totally separate and modular so that each of the variations we are creating is a separate open router API call so that if one fails the others are not affected.

**59:17** · Make these changes.

**59:20** · All right, we're going to launch this.

**59:21** · Now while Codex is working on those changes, let me explain the concept of local host because if you recall this is running on local host. This is not deployed anywhere. It's not on any server. It's running locally on my MacBook. So local host is just a way to turn your machine into a server. So when we go can see the agent run npm rundev earlier, you know, npm run lane build.

**59:44** · If we scroll up, you'll see the npm rundev command which is starting the development server. It's using local host as a temporary server, turning my computer into a server. And another nice thing of local host is that it has what's called a hot reload anytime Codex makes any changes to the app. So maybe I can say like keep the original photo visible u more like more visible, right?

**1:00:09** · Or maybe this text is too big. I'm going to tell it to make this text a bit smaller. update the front end so that this text is a bit smaller font size.

**1:00:20** · Okay, I'm going to paste it in. You will see that this is hot reloaded. I'm going to lift my hands. I'm not going to do any changes. And hold reload means that the changes are automatically implied without you having to kill the server and restart it from scratch. Let's see if the codex okay searching for it. And any second now, this text should be made smaller. There it is. It was made smaller by itself. And I didn't have to reload anything. It's auto reloaded which obviously makes it a lot easier to make changes and develop. However, since this is on local 3000, it's taking up the 3000 port.

**1:00:51** · So, if I were to start a different app with npm rundev, it would go to 3001. Avoid any port conflicts because the 3000 port is already taken.

**1:01:01** · And another nice thing about the local server is that Codex can do it for you.

**1:01:04** · If you look at here, we have one background terminal running, which means Codex is running the server in itself. I didn't even have to open a terminal and type in mp run defaf. Obviously, if you want to do it yourself, you can, but Codex is running it inside of itself.

**1:01:19** · So, it can see the logs, it can kill it, it can restart it. It's just easier.

**1:01:23** · Like, you don't even have to start the front end. That's how easy it has become to build software with AI. And by the way, if you enjoy this step-by-step style of teaching and you want to learn more about AI coding, then make sure to join the new society because this is exactly what you're going to find inside. Inside of the classroom, you will find everything you need to master AI coding within three weeks. And each of these weeks is full of step-by-step modules on different concepts all related to building with AI. So again, if you're serious about AI and you want to get the skill of being able to build anything with AI agents, make sure to join the new society.

**1:01:54** · It's going to be the first link below the video. So now that our project is pretty decent, I mean, it works.

**1:02:01** · We've proven the demo, we've made some changes, let's throw it up on GitHub, right? If you want to deploy it, if you want to share it with somebody else, GitHub is absolutely non-negotiable. So, let's go to github.com. And by the way, if you want to go deeper on Git, GitHub, what are the differences, the purpose of each of them, then uh there's a module inside of week 2 in the new society, module number 17. We have couple of modules exactly on this topic. So, I'm not going to go too much in depth here.

**1:02:27** · Just create a GitHub account and click on top right and click on repositories.

**1:02:30** · Here we need to create a new repo. So, click on new. Let's name it UT mirror because that's the name of the project.

**1:02:40** · Test project for Codex video.

**1:02:44** · Then repository public or private. Most of you will probably want to have private. So make sure to select private here. And then you can click on create repository. That's it. It's as simple as that. Next, we just need to copy this link right here. Copy that and switch into cursor. So again, right now everything is local. Everything is on the laptop.

**1:03:04** · Putting it on GitHub makes it accessible to servers, makes it accessible to other people. If you want to have another developer or you are building something for a client, you definitely want to throw it up on GitHub. So, I'm going to say here is a new GitHub repo. Pasting the link, please push everything in there. Enter. So, the main thing is you need a git ignore, right? We already created one. We have a git ignore file right here. Be pretty comprehensive.

**1:03:30** · definitely better than I would have written it. So I'm not scared of pushing to GitHub um pretty radically here. I would say probably um stage all files and do a commit. We have some changes.

**1:03:41** · This is another beauty of IDE. You can see this uh this icon here. You can see the different changes to the files based on git, right? So I highly recommend you use an IDE because if you are just running an agent in the terminal or using the Codex app, which more on that later, you would not see these changes.

**1:03:59** · Okay, so everything is pushed to git and let's see what's happening. Everything's okay. So now if we reload in GitHub, we should see our codebase. There we go.

**1:04:07** · Our codebase is here on GitHub with everything. We have the read me file, beauty mirror. Amazing. So now we've managed to throw up a local project into GitHub, which makes everything easier. GitHub allows us to deploy to platforms easier. It allows us to share the code with others. And in fact, we're going to deploy it right now. Now let's say you don't know anything about deployments. You don't know what is the best platform, where to host it. Well, guess what? You can ask Codex. And this is what I mean.

**1:04:36** · A lot of you guys are thinking too one-dimensionally about how to use these agents. You think, okay, it's a coding agent. I'm only going to use it for coding. But that's a huge mistake. Codex can help you with all the other parts.

### Deployment: Hosting Your App on Vercel

**1:04:48** · So, so I can say I want to deploy my app somewhere so that it is accessible on the internet for others. What are the best hosting platforms for our app specifically?

**1:05:08** · Analyze the text stack.

**1:05:11** · Again, think harder. Give me top three options. Be very concise.

**1:05:19** · you can consult it, right? This is the beauty of having one consultant and I actually I can copy the prompt. So, right here there's a copy button below every message and I can use the use the cursor agent. I'm definitely going with Opus. It tried to switch me automatically but I'm going with Opus fast and we can check both of them right.

**1:05:39** · So both of them are going to give me a response and can say okay best versel why because it's the simplest and because we have nextjs and versels are literally developers of nextjs and as you can see opus 4.6 agrees so both opus and gbd 5.4 for agree. So we're going with Versell. So now I can say okay let's go with Versel.

**1:06:01** · Give me stepby-step instructions of what I must do. Be very concise because if you don't include be very concise these agents are super they yap a lot super right. So we already pushed it to GitHub. Then we need to deploy Versell.

**1:06:17** · So let's follow these instructions. Go to versell.com and create an account. So let's do that. Boom. Okay. Okay, so on Versel again you can get started completely for free. You'll see something like this once you log in. Now obviously I already have some projects because Versell is what I use for vectal and for all of the internal software that is running NexJS.

**1:06:34** · But if you don't just go to top right and click on add new and project the when you're creating a versell account you should consider using GitHub as authentication method because here you can literally see the repositories and that's how easy it is right I can see beauty mirror right here. So I can click on import and here we can do some advanced settings. Now it's probably good as it is and if you're not sure just take a screenshot again image inputs are so OP. I'm going to copy the screenshot.

**1:07:01** · Go back into cursor and I'm going to paste it in and obviously I'm using opens here but we can be using codex in the extension or codex cli here doesn't matter. We say I'm here. All good. Answer in short.

**1:07:20** · Provide the image as necessary context.

**1:07:22** · Okay. So, actually we should add the uh environment variables. That's good. It's good tip here. Boom. That's why I use the AI agents. Like I'm using it to help me deploy. It has nothing to do with coding, but it's still extremely helpful. So, I'm going to go into the ENV local file. Copy the name of the variable aka key value. And then I'm going to copy the actual API key itself.

**1:07:43** · Make sure to not include or exclude any characters. Boom. And again, do not share API keys. Okay, I'm going to rotate this one after uploading the video or before uploading the video hopefully. Okay, let's click on deploy.

**1:07:56** · And just like that, we are deploying our project on Versell. It really is that easy, right? So, if you've never deployed anything on the web, you have nothing to be afraid of. Deployments in 2026 have become so effortless. And this is why you need to get familiar with GitHub because when you push your project to GitHub, all these platforms have integrations with GitHub. So whether it's Netifi, Railway, Render.com, RCL, Superbase, doesn't matter. These platforms make it super easy. And there it is.

**1:08:25** · It was like 20 seconds and we now have our project deployed. So I'm going to click continue to dashboard. And Versell even gives us custom domain. And here we are. This is a This is a custom URL. This is no longer a local host. This is fully deployed. So, I can use the selfie again. Boom. Boom. I can run it. Maybe.

**1:08:48** · Let's unselect some of these. Whatever.

**1:08:51** · Let's just run all of them. Generate. I want to see if the changes work actually where it was uh like separate because we did a small refactor there. I was telling it to show the results separately rather than waiting for everything. I'm kind of curious if that worked or not. I don't think we've tested that.

**1:09:09** · And yeah, we we're deployed just like that. Oh, there it is. All the changes are here. And as you can see, it works.

**1:09:18** · Amazing. Our app is fully deployed on the web thanks to Codex. I mean, it has built has been fully built by Codex.

### Understanding Sandbox Modes & Approval Policies

**1:09:26** · Now, before we go into the Codex app, which is becoming super popular, I want to explain the different sandbox modes inside of Codex. So layer one is the sandbox mode and this is what codex can do technically and there are three different options. Workspace write which is the default one. This only lets codex write into your project folder. It cannot do anything on the network and it cannot access other folders on your computer. Then there is read only. This lets it read files but it cannot write anything. So this is available in the chat or plan mode.

**1:09:54** · So another thing I haven't shown you yet is the plan mode inside of codex. Right? So when you have let's say ox extension again you can create a new chat here or in the CLI you can do / new you can do what's called a plan mode. So you can do slash plan to switch into plan mode and you can see the purple text here or do slash plan here toggle plan mode and you can see these icons here. This is really good for starting a new project or doing larger changes. Codex will interview you.

**1:10:22** · It will figure out okay the user wants to refactor the back end to be rust and it will interview you like okay why are we doing this how it should look like you know do you want to refactor everything or only the files where speed matters it's going to start asking you questions and basically planning the project so if you are a beginner and if you don't have a clear idea of what you want to build definitely start with plan mode just type in / plan to toggle it

**1:10:46** · either inside of the extension or inside of the CLI and you'll see it right here and before it gets to building it will analyze the entire codebase do a lot of reasoning a lot of thinking to figure out what you want and how the app should actually look like. So when Codex is inside of plan mode, the sandbox only allows it to read only which means it cannot write anything. It cannot change anything. It can only read files. Then there's a danger full access. This is the sandbox mode level. That's obviously the highest one which gives it full access, right? And it starts with danger because it's dangerous.

**1:11:17** · It can write anywhere, access network, use risky commands and um do anything without asking you for approval. But the second layer is actually the approval policy.

**1:11:30** · This is just the sandbox mode. So you have untrusted, on request, never, and granular. Untrusted means it asks before every single action. And this is very annoying, right? Like obviously it's the safest, but also it's not autonomous at all. Like if you had to approve every single command, we would still be building the prototype, right? We wouldn't have the app fully deployed on Versel and on GitHub and fully working with open router and with some changes, right? Definitely not. We would still be stuck building the MVP.

**1:11:58** · So that would obviously be very annoying, but it is there as approval policy. Then you have on request. This works freely inside of the sandbox and asks it when you want to go beyond. So I think this is the default where if you are in certain certain folder, it doesn't ask you. It just builds stuff right in that folder.

**1:12:16** · But if it wants to go into your downloads or your documents or do something else that might be risky, you know, run a terminal commands, then it would ask you for permissions. Then there is never, which uh, you know, never asks you, which is dangerous obviously. And there is granular, and this is like per category control. Now, here are the default combos because these these are just concepts, but we care we care about the actual combos, right? So the default is workspace, right, and on request.

**1:12:45** · This is pretty balanced and this is what most people use. Then there's full auto and you can launch this with the parameters, right? So remember by default if you type in codeex and just hit enter is going to be with these permissions this sandbox level. But if you do space- full auto full- auto spelled like this, you need to make sure it's exact proper spelling.

**1:13:08** · Then it would launch with a bit more permissions. However, as I showed you at earlier, the most permissive and the most aggressive and the most autonomous version of Codex is d- yolo. This makes it dangerous full access. So, the highest level of sandbox mode and never so it never asks for approval policy.

**1:13:26** · So, both layers are fully maxed out and it's it's like turning a car into sport modes or sport plus mode, right? It's just like full performance, full all out, no checks, nothing. best suspension, highest braking, everything to the max. This is how COX YOLO works.

**1:13:43** · And honestly, I'm going to give you a secret of the industry. All of the people who achieve stuff with AI agents use them in YOLO mode, right? So, obviously, this is what it looks like on Codex, but on cloth code, it looks like this. Clash- dangerously skip permissions.

**1:14:01** · This is how it looks like for cloth code, but for Codex is d- yolo. If you want to achieve anything with these agents and if you actually want to build fast, you need to use a yolo mode because uh otherwise you'll just be waiting for approvals, you definitely cannot manage multiplayer agents because they're constantly waiting for you to hit enter. And yeah, it's just not practical at all. Obviously, it is risky, so use it at your own risk. Don't blame me if it, you know, delete some files or whatever. That's why you should use Git, by the way, so that if the agent messes up, you still have your project on GitHub and you can go to the previous version, right?

**1:14:32** · But anyways, this is how the sandbox works inside of Codex. All right. Now, let me show you about the Codex app because this is a really next level step up of how to use Codex and u it's available for Mac OS right now, but it's coming for uh actually it's available for Windows as well. Okay, Linux. It's not available for Linux. So, it started on I don't know why it says, look at this. This is crazy. It says it's available on Mac OS, Apple Silicon, but here it mentions it's on Windows and Mac OS. I think they just forgot to update it. So, if you have Windows or Mac OS, you are chilling.

### The Codex Desktop App: Multi-Agent Management

**1:15:02** · So, just go to this. I'm going to link this below the video. It's the official OpenI documentation. And download it for Mac OS. Save the downloader. And again, you might be thinking, okay, David, why are you showing me another way to use Codex?

**1:15:17** · Well, because this probably is the most advanced one. This gives you the most options and it's the most userfriendly.

**1:15:22** · So, drag this into applications folder and then open the Codex app like this.

**1:15:27** · Boom.

**1:15:29** · This is very new. is the newest version of Codex and uh it's as you can see it's completely different. It's a full application. It's not just a extension or a CLI and it has a very nice user interface and it allows you to do a lot more things that normally you cannot do.

**1:15:45** · So first of all on the left let's add a new project. Click this button right here and we're going to add this uh project, right? This is the beauty mirror that we're building. I say what is this project about? Now, you might already notice a few things, right? We have the model here. We have the reasoning effort. Very similar to the extension. We have the slashfast. You can turn on and turn off fast mode. And at the bottom, we have the permissions.

**1:16:12** · So, this is the default. No codex uh runs in a sandbox. Full access. Boom.

**1:16:17** · Obviously, we want full access. On the left, you can also see like you can run multiple threads in in parallel. So, here I can start a new codeex. And by the way, these are uh these are the sessions. Nice. I actually wasn't aware of this. This is very nice. These are the different sessions from CLI and extension. So, you can continue on them inside of the of the Codex app. So here you can run multiple agents in parallel and all of them each of them has their own separate git work tree which is kind of like a clone of the folder which means they can work on different features without interfering.

**1:16:48** · So if I wanted this guy to say like go over the front end and make it look better and and this guy I can say go over the backend prompts to open router and make them more concise and better prompt engineering. Both of these will be able to run in parallel. You can see on the left they're both running and they will not conflict because each of them gets their own git work. You can also pin any of them. So on the left there's a pin.

**1:17:20** · You can you know move them to the top if they have priority. And here are like your favorites uh threats. They call it threats or chats. And yeah you can see that I have different folders open here.

**1:17:31** · So you can work on multiple projects at once very easily from a single app. And this is basically OpenAI's response to anti-gravity. Anti-gravity is a project from Google that was really good at managing multiple agents. That's where it was revolutionary. Codex with the Codex app is really trying to do their version of that to make it great and managing multiple agents in parallel.

**1:17:54** · And this is really what we're going to see the future development is multi-agent management. orchestrating multiple agents because it's inevitable that all of us are soon going to be running dozens and dozens of agents below us and that's coming very soon. So these companies are figuring out what is the optimal user interface, how to do that on a technological level, on architecture level, stuff like that. So this is the Codex app and for a lot of people this is becoming their favorite way to use Codex because of how many features it is and because of how easy it is to use. By the way on top right you can see the diff editor.

**1:18:25** · So here you can see the changes made in this thread and you can see these are unstaged. So that has been uh did it push to GitHub?

**1:18:36** · Okay. So here we can see the changes here. So if you want to review it, you can see that and even there's the folders they just added that. So they're trying to make it more of a IDE. It's not a full IDE yet, but they're working on it, right? So you can see the the files here and the diff editor here, the primary panel. It's not as advanced as VS Code. Nowhere near. In fact, that's why they still have the open in VS Code button. In fact, you can open it in cursor as well and tag as well. All of the main code editors because they realize it's not a full ID. So, that's why they added that button, you know.

**1:19:07** · But anyways, next let me show you how skills work inside of the codex app. So, let me close the file tree here. Boom.

### Leveling Up with Skills & Plugins

**1:19:14** · Inside of plugins, you can go to in the left side and click on skills. At the top are different skills which are basically sets of instructions for your project. And as you can see, I have a bunch of Appify ones because I used that in the past. But there are a few built-in ones here. Image Gen, OpenAI, Docs, Plug-in Creator, Skill Creator.

**1:19:33** · And you can select them or uninstall them. Right? So let's say if we want to, you know, uninstall this skill, you can just click on that and boom, uh, it uninstalls that specific skill. And if you want to add more skills like soda, PDF, dog, you know, maybe playright, playright is great. Actually this one I would definitely recommend all of you because it gives the agent ability to test the app. Playright is a framework for browser testing.

**1:19:57** · So if you want a if you want codecs to click around the front end test different buttons that they work install the the playright skill for sure. And by the way the skills from the CLI and the ID extension will automatically show up here as well because it's all shared as you've seen with the chat. Now invoking skills you can do with the dollar sign right. If we go into any of these threads and do dollar sign and you can see all of the skills right here. So if we want to do like the GitHub skill for example or let's say image gen, right?

**1:20:24** · Say create a potential logo for this project and put it as the fabric because right now we still have the the default one. You can see at the top there's no fabric in the URL. So I can use the image gen skill which will use the OpenAI image tool. I think it's the V1. They they are rolling out the V2. So maybe by the time you watch this it's going to be the new V2. But it's going to use that to generate an image and then Codex can use that image to either build assets with your app.

**1:20:55** · That's another great thing. If you want to build graphical apps, you know, like a mobile games, video games, um RPG games or anything that requires like custom graphics and assets, you can use the image gen skill to do that. And uh Codex will use the built-in model, image generated model to create that.

**1:21:14** · Okay, it's kind of complaining that it's not the right tool, but whatever. Now, installing new skills, you have multiple options, right? You can use the built-in skill installer skill. So, inside of any chat, if you do dollar sign skill installer, you can install skills with this skill. I know it's a bit of a mouthful. You can also point the installer at any GitHub repo or Codex will auto detect newly installed skills.

**1:21:36** · Actually, in the in the left, if you go to plugins and then click skills at the top, you can click the create button and create skill. And here it will uh chat with you and create a new skill. Another huge feature is the automations. This is basically advanced chrome jobs. So as you can see there are some pre-built ones. Summarize yesterday's good activity for standup. Synthesize this week's PRs. Summarize last week's PRs.

### Automations: Cron Jobs for AI

**1:21:57** · Bunch of other stuff. And a lot of people are saying this is a lot more reliable than open claw. So if you have something you want to do daily, maybe update your documentation or turn the latest updates into a article or maybe scrape new leads. Again, think beyond coding. This could be used to find new leads for your business. You can click plus new automation. Just give the automation title, describe the prompt, select either work tree or local, select the project, when you want to run it, how often.

**1:22:25** · And this is one of the main features, one of the main reasons people are using the CEX app is the built-in automations. And these are way more reliable than openclaw chrome jobs. Oh, and one more thing I want to show you is the sub aents. So I can say launch a sub agent to add header comments to every file in our codebase. Just briefly explaining what that file does. Okay. So code accessibility to start sub aent so that you're not blocking the main chat.

### Dispatching Sub-Agents (Workers)

**1:22:55** · It's it's calling it a worker. But you can see here created with GBD 54 mini. Here we can click on that and this agent is running and you can talk to the main agent. You can see here's one background agent and it can disport dispatch many of them. The beauty of this is that it doesn't block the main chat. So you can keep talking to it and you can keep working with it while smaller agents which are using faster models are doing some of the easier work on the back end.

**1:23:22** · So this has been the ultimate CEX tutorial. We've covered a lot I know but if you watch until the end then I want to congratulate you. You probably know CEX better than 99% of people. And again, if you want to take this to the next level and you want to actually master AI coding, then consider joining the new society. This is my own AI community where in a matter of three weeks, I take you from a complete beginner to someone who can build virtually anything they want with the help of AI coding agents such as Codex and Cloth Code. And here is what that looks like in the classroom.

### Conclusion & Final Resources

**1:23:51** · You can see that there's step-by-step modules, super granular, super easy to follow, split across three weeks that anybody can do.

**1:24:00** · I don't care if you've never used AI, if you're not technical, doesn't matter.

**1:24:03** · You can absolutely follow this and you will master AI coding in three weeks.

**1:24:08** · I'm certain of that. So, if that's something that interests you, make sure to join the new society right now. It's going to be the first link below the

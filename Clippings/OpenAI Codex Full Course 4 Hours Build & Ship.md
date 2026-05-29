---
title: "OpenAI Codex Full Course 4 Hours: Build & Ship"
source: "https://www.youtube.com/watch?v=j7d5rs0iMlE"
author:
  - "[[Aniket Panjwani]]"
published: 2026-05-02
created: 2026-05-29
description: "Go deeper inside The AI MBA Pro — weekly live calls, advanced builds, and direct access as you ship with Codex and Codex ⤵️https://www.skool.com/the-ai-mba-p..."
tags:
  - "clippings"
  - "YouTube"
  - "Codex"
  - "Vibe Coding"
  - "agentic coding"
quality: must-compile
compile_status: compiled
compiled_to:
  - "Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流.md"
  - "Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环.md"
  - "Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架.md"
  - "Outputs/课程与训练营/Codex新手VibeCoding课程.md"
review_note: "Raw/NotebookLM/2026-05-29--youtube--OpenAI Codex Full Course 4 Hours Build & Ship.md"
remaining_value: medium
---
![](https://www.youtube.com/watch?v=j7d5rs0iMlE)

## Transcript

### Welcome and course promise

**0:00** · Welcome to the definitive course on open AI codecs. I use codecs every single day as the director of AI and ML at Paylice, a VC funded fintech startup. I also teach over 1,700 people in my school server, the AI MBA, how to use Agentic coding tools like Codeex and Claude Code for both personal, professional, and also academic research applications.

**0:25** · Now, I also recently made a 3hour full course on Claude Code for beginners. But the reality is that for the last few months, I've been using codecs for 80 to 90% of my work. And my recommendation to anybody new to the agentic coding space is that regardless of your budget, whether it's $20, $100, or $200, is that your first subscription should be to Chad GBT, which gets you access to codeex.

**0:54** · As I discussed in a recent video, there are many reasons for this, and I'll also discuss them in this course. But in a nutshell, Codeex is the best model. It has the best usage limits and it's got the best interface for agentic coding. The codeex desktop app.

**1:12** · In this course, you're not going to have to have any technical background. Maybe you've played around with chatbt or clawed in a web interface or you skimmed through my clawed code course. Either way, I'm going to take you step by step all the way from not knowing anything about agentic coding to being able to deploy a full-blown web app with codecs.

**1:35** · Additionally, this isn't one of those courses where I'm going to fill you up with hours of theory before we get to anything practical. I'm going to give you practical applications of codecs that you can take away and which will add value to your life within the first 10 minutes. And that's going to be a common pattern in the rest of the course. I'm always going to take little bits of theory and get as quickly to practice as I can. Now, one more thing I want to flag before we get started. This course is specifically concentrated on the codeex desktop application.

**2:05** · Codeex actually ships as several different interfaces. There's the command line interface that you have to use in the terminal. There's an extension inside VS Code. And then there's the desktop application. I'm going to be focusing on the desktop application because it's the best interface for agentic coding, but nobody has put out materials that teach people how to use it yet. In the desktop app, you can easily run multiple codeex agents working on different aspects of your project in parallel.

**2:36** · Set up automations which will run on the background on a timer and review all of it in one place. Let me first give you guys a brief overview of everything that we'll be covering in this course. We'll start by talking about what codec actually is. It may be unfamiliar to some of you, how much it costs, how to install it.

### The 24-section roadmap

**2:55** · I'll give you a tour of this desktop app interface which may be new to some of you who may be used to a terminal interface and then we'll start getting directly into some of the fundamentals of agentic coding such as context windows and compaction and why you should typically be using voice for most of your work with codecs. Next, I'll cover some of the basics of agentic workflows past simply using it in a sort of chat GBT sort of way. We'll talk about permissions, guardrails, and just the basics of what you need to know about terminals.

**3:25** · I'll talk about this agents.md file, which gives codec context about what to do in a project when it's starting up. And then we'll start getting into what I call the five practical primitives of agentic coding.

**3:39** · Those are command line interfaces, skills, mcps, plugins, and sub aents.

**3:44** · We'll talk about plugins and the plug-in system in codecs. We'll talk about a particular plugin called computer use which allows codecs to control every single application on your computer. And then we'll do a deep dive into skills which are a fundamental concept in agentic coding to give agentic coding tools the ability to do repeated workflows with all sorts of external systems.

**4:08** · I'll compare this with an alternative way of getting access to external systems called MCPs and then we'll go into sub agents which allow you to parallelize work allowing you to do things a lot more completely and quickly. We'll talk about when to use which of these different tools and then from there I'll start bridging into the last third of the course where we talk about how to go from doing automations on your computer to building full-blown web applications.

**4:36** · And the first prerequisite to understanding this is to understand the version control system git and how it interacts with GitHub.

**4:45** · Then I'll take you through a sort of product agentic coding course where we'll go and learn how to use agentic coding tools to think about what you want to build from a product perspective. And there's particular skills that I'll introduce to help automate this. Next we'll go into the idea of cloud delegation running agentic coding tasks in the cloud instead of your local computer. After that we'll get into GitHub issues which I find to be a very useful basic project management tool.

**5:16** · And once we have GitHub issues in place automations become very useful. This is a concept in codeex to have certain sort of workflows that run on a timer. And so you could imagine for example checking in every single few hours what sorts of new bugs arise and perhaps if they're simple automatically starting up on solutions to those bugs.

**5:39** · That's the kind of thing that you'll be able to build after going through this automation section. Then for the application that we're building I'm going to introduce the general stack that we're using of Nex.js JS the front-end framework, Convex the backend framework, and Versell the place where you host your applications. After introducing the stack, I'm going to introduce the concept of work trees, which are a little similar to sub aents, but instead allow you to parallelize work across an entire repo rather than just within a repo.

**6:08** · And this is very powerful to be able to scale up the rate at which you're able to complete agentic coding tasks. Then finally, we're going to build out this creator carousel studio. So, I'm going to build a kind of social media creation automation. Now, this app which I'm going to develop may not be relevant to every single person who is taking this course, but I still do recommend you go through this section if you're interested in general with app development.

**6:37** · Because what's important to get out of this section is different methodologies that I'm going to show you on the fly. Both simpler ones, both less automated and more automated, more handsoff workflows when you're building any kind of complex web application. And the nice thing is that you're not going to need to know about the deep technical foundations of what you're building because I'll show you how with natural language just expressing your intent, you're able to build fairly complex applications by yourself.

**7:09** · I'm going to create a companion skill to this application so that we're able to interact with it both in a web UI and from our local computer and then we'll deploy it so that it's available on the wider internet. All right, let's get started. So, first, what exactly is Codeex? If you've used ChatGpt or Claude in the browser in the past, you know how it works. You open a tab in your browser, you type in a message, and then the AI responds.

### What Codex actually is

**7:37** · You can upload a document and you can ask it to write some code, but it can't access the actual documents which are on your computer, and it can only run code in a very limited sandboxed environment. It can't run code actually on your computer. That's the fundamental problem which Codeex is here to solve. When you run Codeex, it's running on your computer. So, it sees your actual files.

**8:02** · It can edit them and it can run commands whether to test some code or move files from one location or to another or to do really anything you can, it can also do from your computer. The analogy I gave in the Claude code course, which also applies here, is that things like Chad GBT and Claude are like asking a friend for advice. And then Codeex and Claude Code are like your friend actually sitting down at your computer and then doing the work for you. Now, Codeex starts with code.

**8:31** · And so you might think that this is primarily a coding tool, but really since it's got access to your computer and to your files, it can do and help you automate anything that can be done with access to your files and your computer. So for example, you can use Codeex to draft emails, analyze PDFs, analyze your business spreadsheets, or even help you do your taxes. If it's on your computer, Codeex can help you out with it. Let me show you a quick demo right before I get into installing Codeex. Here we are in the Codeex desktop environment.

**9:03** · So, if all of this looks very unfamiliar to you, don't worry. I'm going to be getting into that in just a few sections. What I wanted to show you quickly is just a practical demo that shows you the power of Codeex and which you'll be able to do right after going through the very next section. As you can see right here, Codeex ships with a file browser. And this is the directory that I use to organize all my research and my thinking about different YouTube videos.

**9:30** · And so, one thing you can see here is that I have a folder with about 10 different PDFs of different papers on AI job loss.

**9:40** · And let's say I wanted to make a summary of all of these PDFs. How can I do that?

**9:46** · Well, I'm simply going to come in here and say go to the content directory for 2026412 AI job loss and then I want you to create a sub agent to read every single paper in the research sources PDFs directory and create a detailed summary of the paper and different angles that might be good for YouTube videos.

**10:12** · Then I want you to take the markdown created by each sub agent and compile it all together in one attractive PDF using Pandock and IceBogle. Now, if that all sounds like gobbledegook to you, I totally understand cuz I haven't explained anything yet. But I just kind of want to prime you with some ideas because we're all about practice. We're not about theory. We're about practice.

**10:41** · And so I want you guys to see the power of codec at a kind of basic skill right now or like a basic task right now but which is likely to be very useful to you all. You may have lots of different documents or papers across which you want to do some kind of research. And this kind of thing that I'm doing right here, it doesn't get rid of the need for actually doing your own reading. In fact, if you look over here on the left hand side, you're getting a little bit of a taste of what's to come.

**11:11** · This is where you can see all your project. And you can see here that I'm building my own PDF reading app. I'm even building my own focus app. And I'm building my own general learning system for how I like to learn things in a gentic way.

**11:26** · All right. So, Codeex now in parallel is doing research across many of these different PDFs and then it's going to come back to me with some kind of comprehensive summary. All right, it finished. Let's take a look. So, we're going to click this open. And one of the nice things is that these briefs can open up right in your browser. So, let me close the file tree. AI job loss research packet detailed paper summaries and YouTube angles. And then I've got like 10 different papers in here.

**11:57** · So let's take a look at this. I guess I can't click on it, but still pretty cool. Let's make this a little bit more small. And so this is nice. So I would often take something like this and just stick it on my phone. And now I have something to like keep my mind running while I'm on the go in an Uber, at the gym, whatever.

**12:20** · So, this is a pretty cool first demo that I wanted to show you guys of the power of codecs and something that's really not possible when you're just using these tools in the web UI. All right, so how do you do something like that yourself? Well, first you're going to have to install the Codeex desktop app. So, that's what I'm going to get to now. Let's talk about installation and also pricing for Codeex. All right. So, as you can see here, codeex is included in your chat GPT subscription. So, which subscription should you get?

### Pricing and installing Codex

**12:50** · Now, technically, you would be able to use codecs in a very lightweight way on the free or go levels, but the minimum that I suggest to most people in order to get the latest models and have even a decent amount of usage is the $20 per month plan. Now, if you're on the $20 a month plan, it is very likely that you're going to hit your session or weekly usage limits.

**13:17** · So, if you come in here to the Codeex desktop application, click on settings and then click on rate limits remaining. You see that it tells you here in the bottom left corner in every 5hour window how much can you use and then also on a weekly basis, how much do you have left? So, I'm actually likely to run out of my weekly limit pretty soon, and that's on the pro plan at $200 per month.

**13:44** · Now, I use Codeex extremely heavily because I'm working with multiple coding agents across many projects simultaneously, but what I would recommend for most of you is to get on the $100 per month plan, which gives you five times the limits of the plus plan. I'm on the $200 per month plan, which isn't listed here, but that's why it says from and then it's a 20x and so I have even higher limits.

**14:11** · Now, one thing to note here is that you can also use codecs by the API. I don't recommend that because the subscriptions are giving you a subsidized rate for the amount of usage that you get. So, choose whichever subscription makes most sense for you. Next, you'll want to install Codeex. And you'll see here that there's a command line interface and then a Codeex app.

**14:36** · Now, this command line interface is actually mostly open- source, which is a pretty cool feature of Codeex as opposed to Claw Code, but we're going to be focusing on the desktop app, which is both better, surprisingly for beginners and for power users. So, you come over here to developers.openai.com/codex/app openai.com/codex/app.

**14:59** · And then you can install it either for Mac or for Windows. So I would just click on the one for Mac. Then once it's installed, it's going to show up over here in your downloads. Double click on it, grab it, drag it, then say replace if you've already got an old version.

**15:18** · Now you can open it up. You'll see something like this. Press come up. Say open. Okay. Now there's two options. You can continue with chat GBT or enter an API key. You should have a Chat GBT subscription now. Sign in with your email address. Say continue there. And then if this is your first time in Codeex, you're not going to see all this stuff on the left or any of these things, but it remembers that I had Codeex installed before. So I get to come back to my previous state. All right.

### Codex Desktop interface tour

**15:50** · Now, before we do any deeper exercises, I want to give you a full tour of the desktop application. I'm going to go through every single interface, explain where it is, what it is, and how to use it. We're not going to go fully into detail, but I want you to have at least a cursory overview, and then we'll go more into detail later in the course. So, this is what you see when you launch Codeex. On the left hand side you see different projects each of which are defined by a particular folder.

**16:22** · If you want to add a new project you just click this add new project button and then if you like me have a projects folder where you like to keep everything you can either have a new folder and create a folder in there.

**16:37** · Open it up and now the files and work that codeex does will by default be done just in that folder. And so I can scroll here and I can see that there are different threads here that have been created for a wide variety of different projects. And then if I want to start a new chat in some project, I just come here, click on new chat. I can choose between my different projects that I have available.

**17:03** · And then I can simply ask codec make me a Python script to make a map of the United States in a virtual environment. And so now Codeex will start working and the UN user interface has changed a little bit. Now here we can see the work that Codeex is doing which includes running various commands and then down here there's an interface in which I can ask for follow-ups or whatnot.

**17:32** · Now we'll come back to this but I want to show you a few more interfaces. Next besides this new chat button we see a search button.

**17:42** · So if I wanted to look for example uh in which where was I talking about making a Spanish course? So, I'm making Spanish versions of some of my materials. And so, you can use that to find a thread when you have lots of projects and lots of threads in each project. Then, this button for plugins is where you can see different plugins which are available in codecs. You can think of these as capabilities that allow you to connect with external systems or to do things that codecs otherwise couldn't do.

**18:12** · So this one, the computer use plugin on which I recently made a video and we'll be talking about in more detail later in this course is a plugin which allows you to control Mac apps from codecs. But if you come here and select this built by open AI plugins, you'll see that there are all sorts of plugins for lots of different things. So there's like a Figma one, Google Drive, Gmail, Slack, etc.

**18:40** · So, we'll be experimenting with some of these plugins later in the course, but I just want you to be aware of them for now. Now, also, if you look up here on the top left, you'll see there's plugins, but also skills. So, skills are a concept similar to plugins, but they're perhaps more specialized particular capabilities. And some skills come bundled with codecs. And so you can see for example that there's a skill to create skills and a skill to install skills that comes bundled with codeex.

**19:13** · Now if for whatever reason you didn't want to have this skill available, you could just come here and choose to disable the skill and then enable it again if you wanted to enable it again.

**19:25** · We'll go more into detail on what skills are, how they work, how to make them, how they defer from plugins and other things like MCPs and CLIs, which you might have heard of. Doesn't matter right now. We'll get into it later in the course. And I also have tons of plugins that I've made across many different projects. So you can see some of them are all in here and you'll be able to see all the skills that you make over time whether they're for particular projects or general ones that you always want to be available all the time.

**19:53** · An additional concept that codeex has is that of automations. And so these are literally automations just things that run on some schedule like every single day at a particular time. And so for example at Pay Slice where I work as a director of AI and ML I have a standup summary plugin which I have run every single day before our weekly standup just to summarize the changes that have occurred in the git repository.

**20:23** · And this is useful for communicating both to the rest of the team what I've done in a summarized way, but also for me to get insight into what the other engineers I work with have been working on if I haven't spoken to them recently. And so you can create all sorts of automations in this interface. Again, we'll be getting into this in more detail later in the course. So if we come back over here to this pane, I want to show you a few more features about what's available in this interface.

**20:55** · Now sometimes to install certain kinds of software, maybe you don't want codecs to just do it for you. Codeex can do software installation for you. And if you want to be able to do it yourself, if you're on a Mac or on Windows, often too, what you want is access to the terminal. Now, in this course, unlike the clawed code course, I'm not going to go into the terminal in detail because the desktop app is such a beautiful amazing interface that you end up not really having to use codecs of the terminal or the terminal very much.

**21:27** · But if you want to use the terminal, there's two ways to do it. One is that you can click this button over here for the terminal or as you can also see, you can just toggle it on with command J.

**21:38** · And so that's what I'm doing right there. Command J. That gets me to a terminal. And this terminal opens up in the same folder that you're in. And if you go to another one, there will be a different distinct terminal in each project and each thread's interface. So there's no risk of them interacting with each other. If you want to open multiple terminals in a single interface, you can just click that plus button. And so that's handy to have. Now the next button over here is for toggling the file tree.

**22:08** · So you can see all the files which are in your project and if you click on them you can even look at the file itself. Now most of the time I almost never have to edit files by hand anymore but in the rare occasion that we do I don't recommend doing it within codeex. I instead recommend doing it with an external application.

**22:31** · The particular application that I recommend you have installed is Visual Studio Code, which is a very good, very useful external editor. So, you just look up VS Code, then you'll have a download, install it. You're all pros at installing software. I'm sure I don't need to show you how to do that. In order to easily open up a folder or a file in a particular editor of your choice, you need to first have a git repository initiated in your project.

**22:59** · So the way I would do that is just ask codeex, can you create a git repo for me and make a first commit. Now if you're not familiar with git, don't worry.

**23:14** · We're going to be getting into that later in the course, but basically Git is a version control system which helps you keep track of changes to your files in your project as you work on it. And Git is both really good to use for a variety of reasons as a software developer or for anybody really working with files at all, but it also is very

**23:39** · helpful for agentic coding tools like codecs to give them memory because they're then able to see all the changes that have been made in a project and that helps them do better work. And so if you look here at the top right, you'll see that the user interface has changed a bit. There are a few new things that have come up. So there's this menu that has come up now which with which you can choose to commit, push or create PRs or create branches.

**24:09** · Again, these are git concepts that I'll get to later in the course. But you can also now choose to open up this project in an application of your choice. And so cursor and VS Code are two editors that I have open. The one that I just recommended you install is VS Code, but you can also open it up in a terminal or if you're building some application, then you can build it up in Xcode or Android Studio. So I'm going to choose to open this up in VS Code. Let's click that. And there it is. Now it's open up in VS Code.

**24:39** · And so this can be a nicer environment. It's like more particular to looking through your files. and you can customize it with extensions as you like. And so for most of you, even though I do recommend Codeex for doing most of the operations that you'll need done, having VS Code available will be very useful. Next, you'll also see this other side panel available. So, I can flip it out. And in that side panel, one of the things that you could do is to see files. But there's two other things which are cool to know.

**25:10** · There's a review UI. So, this helps you see the different changes that have been made in your repo as changes are made. Can you make it prettier? And so, I'm going to ask codeex to fulfill this vague instruction to just make the map look more beautiful. And then we're going to see the changes come up on here, but they're just going to be the changes relative to what the last change is that we committed is the git term to git. All right.

**25:41** · So, we've pretty much talked at this point about the main UI, but we haven't really talked yet about this very important interface down here, and there's actually quite a lot going on in this small space. So, let me go through it piece by piece. First, this thing is now making changes. It deleted one file.

**26:00** · And so, as you can see, we can now see these changes coming up on the ra right hand side in this review user interface.

**26:08** · So in this UI when codeex has finished doing something you can chat with it just like you would chat with chat GBT and so let's say uh I wanted to just say make it prettier after this. It would be able to understand that instruction and then try to fulfill it to the best of its ability. But there's also some additional capabilities just in this little text area. So first I'm going to just press in slash and you'll see a bunch of things come up.

**26:37** · Now these are inbuilt capabilities in codeex which are neither plugins nor skills. So plugins and skills as you saw were these sort of specialized things that codeex has to be able to interact with different external systems or give it new abilities.

**26:56** · Everything that shows up when you press slash up top are the default things that come baked into codecs. These aren't additional capabilities. And so one of these for example is fast. And so, as you can see, what fast basically does is it will give you faster inference, meaning you're going to get the responses from codecs faster, but the cost is going to be that you're going to spend your tokens, your weekly limit twice as fast.

**27:25** · And so, I'm going to show you this full settings UI later, but as you recall, if you click on settings and then go to rate limits remaining, you can see what your 5h hour and weekly limit remaining are. So, if you choose to have fast on, then you're going to be going through your tokens a lot faster.

**27:43** · You can also do things like see your different MCP servers, which are available. Some of you guys may be familiar with MCP servers. If not, no worries. We're going to get into it later in the course. You can also compact your thread, which is a way to summarize everything that's been done in your current thread and start fresh.

**28:03** · Again, we'll also get into that later in the course. You can choose the particular model that is used. So right now I have it set to GPT 5.4 and there's also a few others. So that's what slash does. Now if you do dollar sign then what comes up at top are the skills. And so these are these specialized capabilities, most of which I've made myself or which other people have made and I have installed in my own system to allow codecs to do other specialized things.

**28:35** · And so if you want to instantiate or use one of them in your current context, you can use dollar sign. Finally, the last sort of shortcut I want you to know about is at. And so when you use at, it's going to surface agents that you may have installed, but also plugins, which are a concept we talked about. We'll also get to agents and sub aents later.

**28:58** · But you can also, if you want to reference a specific file for whatever it is you're doing, you can reference that file by like going like that, typing it in, and now Codex will know that whatever you say next refers to or needs to include as context that file. Now in this user interface you can also paste in images or PDFs if you want to give those as context to codecs.

**29:23** · So something I do pretty frequently is we can click this and something cool is that HTML files and images along with PDFs can be viewed right in the user interface. And so what I could do if I wanted is just take a screenshot, drag it right in and say, "Can you mark the state capitals as well?"

**29:46** · And you know, that instruction didn't really require me to take the screenshot, but let's say I wanted to say, "Hey, it looks kind of ugly. I don't like this map, but hey, take a look at this map. It looks better." Most of Open AI's models and all the ones which are available in the Codeex desktop app are multimodal, meaning that they can sort of see images and text. And so you'd be able to use them in that way, too. Now, the last little detail I want to mention is this button over here for voice dictation.

**30:21** · So, we'll talk about this in a little bit later in the course, but if you want to give voice instructions, you can just click that. I am the walrus goo. Press stop and then your very important instructions will come up into the interface. All right, so we're almost done with the interface. The last main thing I want to talk about is models and tokens. So, if you look over here, you'll see this little dial.

**30:47** · And that dial is telling us how much of the context window, meaning the available maximum limit of a given thread, has been used. And so, it says 25% of the maximum available context has been used.

**31:05** · We'll get into more detail about what takes up the context window, but one of the main things and you can see that it's increasing as codeex does more things is the files it's reading and the messages that we're giving it and the messages that it's giving us back. The next thing you'll see here is a model selector. So there are all sorts of models and you'll see that some of them are marked as codecs and then some of them are marked without codecs. So what I recommend generally to everybody here is that you just use GPT 5.4.

**31:36** · It's kind of the best model right now in my opinion for any coding task, any any task really for anything other than writing for writing clawed code. Opus 4.7 is pretty good for pretty much everything else. GPT 5.4 is the best model available right now. Now, what often happens after a new model release is that Open AI will come out later with a model that's optimized for coding tasks.

**32:06** · And so, before you used to be able to see GBT 5.3 and GBT 5.3 codeex and so I would use GBT 5.3 codeex to do my coding before 5.4 came out. For now, I just recommend you use 5.4. So because it's such an such an important toggle, it's available right here in the interface, but you can also toggle it by going slashmodel and then choosing your model from there. The last bit you'll see here is this button for reasoning effort.

**32:35** · And so you can choose to have your reasoning effort at low, medium, high, or extra high. And roughly reasoning effort refers to for a given model how much time it's going to spend in a thinking stage before doing something. Now generally I would say that if you add additional or higher reasoning effort you get better results but it's not perfectly the case.

**33:00** · And often when I want to get things done fast or I'm working on something simple I'll switch to medium but most of the time I have it on extra high. If you're on a $20 per month plan, it might make sense to not use extra high that much or stay mostly on medium, probably later in the course, I'll talk more through strategies on how to conserve tokens.

**33:24** · If you are primarily using a $20 per month plan, if you're on the 100 or $200 per month plan, I would mostly just recommend using extra high as your default for everything. That's how I use it. Just a few more comments about these models because you may hear about some of them. So, uh, Mini is a model that I don't really recommend for coding, maybe for certain simple things and codecs used to have this ultraast codec spark model.

**33:53** · Again, I didn't really find any particular use for it, but I just want you guys to be aware of those two as well. Now, over here on the left hand side, you'll see two toggles. one is this plus sign and then this thing which I currently have set to full access. So by default codeex will run with default permissions.

**34:13** · And so that means that it's allowed to do certain things in the folder that it's in, but it's not allowed to do things outside that folder or it may not be allowed to do things without asking for your permission such as installing applications or going to certain websites. Now, I usually leave it on full access, which is a little bit more dangerous because now codecs can go all over my entire computer and pretty much do anything.

**34:41** · But in the next section, I'm going to talk about how to stay on full access, but still make that safer. Not the next section, but in the next few sections. So, we'll talk about the permission system in much more detail, but I prefer having it on full access. It's just a little bit faster.

**34:58** · I'm comfortable with it. So that's where I've got it. And you also see this plus sign here. And so you can add photos and files just like I showed you adding the photo. There's also this concept of a plan mode. So when you turn plan mode on, codeex will not actually write files. It will read files, but it'll make a plan of whatever it is that you want it to do. And so this is generally a good practice when agentic coding.

**35:22** · But my preference for many reasons which I'll talk about a little bit later in the course is to just make plans on my actual file system like not go to a separate plan mode. And so if you've got it on, you can turn it on with shift tab and then turn it off just by clicking on it. I'm going to leave it off for now.

**35:44** · You can also access your plugins right here. So I showed you that you can access them with the app symbol. And over here you'll see that there's a few different options for how you can use codecs. So you can use codecs on the web. You can send it to the cloud if you set up a cloud environment. And you can also hand off to a work tree. So I'm going to teach you all about work trees because they are very useful.

**36:08** · I'm not going to teach you so much about cloud usage because I don't find it that useful and I'll explain a little bit why when we talk about work trees. And finally here, if you're familiar with the Git system, one of the main concepts in Git is a branch. We're going to talk about branches later, but just so you're aware, you can create and check out new branches from this UI or switch between your different branches that you have available over here. So, we can actually see this thing got regenerated. I guess I got to refresh. Ah, there.

**36:40** · And now we've got the state capitals in here.

**36:44** · That's pretty cool. All right. The last bit that I want to tell you about in this interface is the settings UI. And there's a lot in it that's not that important, but I'll try to walk you through some bits which might be more important. So, first here in the configuration tab, there's a user interface in which you can add some configuration options to codecs.

**37:05** · And a lot of codeex's configuration is defined in a file called config.toml which is located in a specific location on your computer. And so if I open it up here, we'll see that this is what this configtoml file looks like. Now most of you will never really need to edit this by hand, but it is important to know that it lives in your home folder in a folder calledcodex. So just important to be aware of.

**37:37** · And you can also in this section make some changes to how the permission system works on your computer. Again, we'll get into this a little bit later. Now, over here in the threads UI, you can see that if I click on this, I can remove some project if it's not relevant to me. But I can also once a thread is not useful to me anymore, I can archive it. So, this is an old one that I don't really need anymore is I can go here and then archive that thread.

**38:05** · But then if you ever wanted to recover an archived thread in your settings, you can come here to archived chats and you'll see all these different chats. You can try to find the one hopefully by its name or the timestamp or the project name and click unarchive to unarchive it. There's also some user interfaces here for Git.

**38:28** · You really will never need to touch this. You can just leave it on its default. for environments. I'll teach you about these when we get to work trees. Again, here for work trees. We'll talk about this in more detail once we get to that. This one for personalization, I don't find that important. I just leave it on friendly or you can put it on pragmatic. Up to you. And then just some general config options for how you like your codec UI to look. Lastly, codec updates pretty often. And when there's an update available, you'll see right over here an icon that says update.

**39:02** · So you just select it, press it, it'll restart, and that'll do an update. Otherwise, you can always go here to codecs, check for updates, and update it from there. All right, so we just covered the entire interface, and you now know enough to get started with codecs on your own project. Just open up a folder, start up a thread, and then start prompting away.

### Context windows and compaction

**39:25** · But next I want to introduce a fundamental concept that you're going to encounter quite quickly as you get started with codecs and that is the idea of a context window and compaction. As I had mentioned right here in codeex there's a dial which tells you how many tokens you've used and how many you have left until this compaction event occurs.

**39:49** · But let me go into a little bit more detail what a token is, what the context window is, and what compaction is. A token in the context of agentic coding and large language models is roughly a word. And so you have limits on how many tokens you're allowed to use at a time in a given conversation. And so what counts as tokens? Well, obviously like if you're giving a really long message, that's going to have more tokens and so your your actual messages count.

**40:20** · But Codeex's responses also add to this maximum number of tokens that you can use. But now that we're in the Aentic coding world as well, the files that it's reading are going to count. So if it's reading bigger files, that's going to use up more of this token limit. Now, Codeex has access to tools to run commands on your computer, to search for code, to fetch things on the web, and the output it gets from these tool calls are also going to count towards your tokens.

**40:51** · Finally, as I've mentioned, there are these concepts called MCPs, skills, and plugins, which we're going to get into later. And the use and the awareness of these tools has some token usage for codecs as a default. And then finally, your system prompt, meaning the prompt that codeex always has in memory to tell itself about what it is.

**41:14** · Your agents.md, which we'll get into a little bit later, but is a description that you can create of your project with project specific instructions for codecs also eat up tokens. And so I've got here 258,000 tokens available in this thread. And it says that this compaction thing is going to happen once it reaches that threshold. So what is compaction?

**41:40** · What compaction basically does is take all these things that are using up tools that I just talked about and it efficiently creates a summary with references to some key decisions that were made here and important files so that codeex can just keep working after hitting that limit. Start not totally fresh but freshish and then keep going on with new work.

**42:07** · This graph here is from anthropic and it shows the performance along a measure called mean match ratio. You don't have to understand what that is but the basic idea is that as we have more tokens the performance of most of these models gets worse over time.

**42:25** · The model performance also becomes more expensive as you're having conversations that use more tokens because effectively what's happening every single time you send a new message to Codeex is that Codeex sends all the previous messages back to Open AI's API and then sends you a response and adds that on.

**42:48** · But there's going to be this kind of pyramiding that occurs as you do this over time where the amount of messages or the size of the message you're sending is bigger.

**43:00** · And so if you're frequently going all the way to the end of your potential usage, you'll see these rate limits decrease more quickly. Now, in practice, what I do is I just let it automatically compact all the time. So, I'm on this $200 plan and I come up close to my limits, but not all the way there. And so, I'm making the most out of my usage and I don't feel the need to do this compaction earlier on my own.

**43:26** · Instead, I just leave these threads running really long and I have various strategies that I'll talk about that I use to make sure that codeex stays on top of work across long running sessions. But if you ever want to do this compaction early, you can come here and just do /compact. And if you have something that you want codeex to focus on in the compaction, you can say focus on new post hog features.

**43:56** · So this is a project I was just working on right now and maybe I would want it to focus on something in particular. I can just say that in the compaction instruction. That's basically all I wanted to tell you about context windows. It's a pretty straightforward concept. You're going to hit this compaction event often. And my recommendation to most of you is just let codeex do the compaction for you.

**44:19** · That's the easiest way to go about doing things. The next topic I want to cover briefly as a fundamental of agentic coding is voice mode. Now, we saw this little voice mode feature earlier when I was introducing the interface. And you can use it by just going CtrlM and then saying whatever it is that you want to say. And then you can just do CtrlM again and it'll show up here on the screen.

### Voice mode and better prompts

**44:44** · Now depending on how I edit this, you may not see how slowly or quickly it showed up, but it was kind of slow. The tool that I like using for voice input is Whisper Flow, which costs money, but if you have an academic email, you get 3 months for free. And there are lots of other free options that are hosted on your computer that people are coming out with to do voice input. But sort of initial question is why use voice input at all?

**45:14** · Why am I emphasizing this as an explicit section of the course? Well, fundamentally, one of the best ways to get better results out of codecs is to give it better context. So, if you're giving more complete instructions with more context about what you want for designing an app or every little detail of how you're thinking about some research problem, then you're going to be likely to get better results.

**45:41** · But when you are typing you can on average let's say type at just 40 words per minute whereas you can speak at 150 words per minute. So just naturally by speaking as a default mode of working with agentic coding tools you're going to get better results. So here's an example of the kind of thing that I might myself do behaviorally if I was giving instructions typed versus giving instructions spoken.

**46:07** · So the spoken instruction is going to be a lot more natural but also a lot more effusive. And so the same person with the same intent is likely to get better results from codeex when speaking right on the first try. Whereas if you say fix the login bug, maybe Codeex is now going to ask you for clarification questions, go off in incorrect directions, and use a context which doesn't help you solve the problem.

**46:34** · On whisper flow, I have control space mapped to the text to speech or rather speech to text usage.

**46:42** · So if I wanted to do the same thing here, I just do that and then I do control space again and it showed up.

**46:48** · Again, depending on how I edit this, you wouldn't see it, but there was like a five or 6 second lag when I was using voice mode over here, whereas it took about 1 second for that to show up. And that may seem like a small thing, but when you're using with these tools, uh, you get kind of annoyed if there's a 6-second lag before some action occurs.

**47:08** · So, I would recommend Whisper Flow if you have the budget for it, or especially if you can get that academic discount. Otherwise, there are other free options coming out. And the in-built controlM voice input option is not bad either. All right, that's it for voice mode. The next thing I want to get to is the permissions system and guard rails in Codeex. So, one of the things I covered when I was discussing codeex's interface is this thing right here.

### Permissions, guardrails, and terminal basics

**47:34** · You can choose to either have full access or default permissions as the two ways in the codeex desktop app to give codec permissions over your computer. So, what does this exactly mean? What is this sandbox? and what is full access and what are the risks with full access to demonstrate the difference. Let me first give you a little bit of a demo using default permissions.

**48:01** · So, I'm going to use Whisper Flow and I'm just going to ask, can you look at my downloads folder or actually look at my desktop and help me clean up all the screenshots over there? They're kind of like messy. I don't like them. So, I have like I don't know two years of screenshots which are all in my desktop folder. And we're going to see how with default permissions codeex does at helping me clean that up.

**48:29** · In order for codeex to move a little bit faster, I'm going to tweak down the reasoning and then say to continue. So, let's try that. All right.

**48:38** · So here we got the first sort of useful example to show the difference between default permissions and full access. So as you can see here, Codeex was able to run certain commands like ls, which just helps it list files and find which is a Unix command to help it find files without needing to ask for permission.

**49:00** · But now it's come to something where it actually wants to move files from one location to the other. And so what it's suggesting is that you've got like 1.1 GB of screenshot files and I can move them to a location where they'll be sorted and leaving other desktop images alone. And so two options come up here.

**49:19** · One is that I can just approve this action. Second, I can say yes and don't ask again for commands that start with this. So I'm going to say that I'm going to say just yes right here and then let it move forward. Now having default permissions on is very helpful and useful because if something dangerous is potentially going to occur then you can vet the action before codeex is able to do that. But there is also a cost to working with codeex primarily in this way.

**49:51** · Sort of the magic of agentic coding is when you can actually let it loose and be able to work for long periods of time with your hands totally off. And so setting it to full access on the other hand won't continue asking you for permissions when these stages occur. So now if I proceed in full access I can say what do you recommend next. So it's recommending a sweep of what remains on the desktop and then stop the mess from coming back. So I'll say sure do that.

**50:26** · The issue with full access is that potentially codecs could delete things that you don't want deleted without you having any mechanism to recover those files for example. And so one option is to give codecs very fine detailed permissions of what it can and can't do.

**50:46** · And that is possible in codeex. Let me show you how. On this documentation page for codeex, there's a pretty thorough explanation of all the different types of configuration options you have at hand to limit codecs on what it can and can't do. So here, for example, you can decide whether to enable full internet access or just have an allow list of particular domains.

**51:12** · You can also have a deny list for what is allowed or not allowed for codecs to read or write on your computer. And all of this occurs in a file called config.toml which is located in a particular location on your computer which I'll show you in a little bit.

**51:31** · There's also a concept called rules with which you can define particular commands that codeex is allowed to run which go on outside the sandbox where the sandbox for a given project you can roughly think of as being that folder like a set of operations that it's allowed to do outside that folder. Now this rules setup is not trivial. It is a pretty complex format that if I was writing, I wouldn't want to write by hand.

**52:04** · I would probably ask Codeex itself to help me write this thing. And I'm personally comfortable enough with these tools that I just leave them in full access all the time. So my recommendation is to either just use default permissions or full access, one or the other. the permission system. You can dig into it and I'll send you those links, but it can be a little bit complicated, a little bit finicky, and so I'm personally comfortable with full access.

**52:33** · But there is one additional tool that I use alongside full access in order to make certain destructive commands impossible for codecs to run. The tool I use for that is called destructive command guard. So, if you just search that on Google or you can see in the slides I'll have in my school server or in the description below this link, you can find this tool.

**52:59** · And basically what it does is it prevents codecs or clawed code really any agent from running certain types of catastrophic commands like get reset hard which is very bad to do on a git repository rmrf source. So you'd want to prevent codecs from accidentally deleting some directory or dropping a table in your database. And so if you want to install this tool, you simply copy this right here. Copy. Then come back to codeex.

**53:32** · And as you recall, in order to open a terminal, it's command J on a Mac, probably similar on Windows. I'm just going to paste that in here and then press enter. and we'll see that it's now active in codeex with this DCG hook. Now that begs the question, what is a hook?

**53:53** · So hooks are an extensibility framework for codeex such that after certain points in the agentic life cycle, some actions can occur deterministically. But as you see here, this is an experimental feature. So in our case what we want is that before any tool is used meaning before any command is run we have DCG run to check if that command is a safe command and if not it rejects that command.

**54:24** · Now in order to use an experimental feature like this you have to open up this file that I was referencing called the config.toml file and add this line underneath features in your config.comtom. So how do you do that? Well, you come here to codeex, then go over here, go to settings, then come down to configuration, then over here, choose global. So that we go to the user configuration, and then click this button for open config.toml.

**54:54** · So let me do that. Okay. So if you've set up VS Code, it should probably open up like this in VS Code. And then I recommend doing a CtrlF for features. There it is.

**55:09** · And you'll see over here that I've already added this line hooks equal true. So if you haven't add that, but if you have, leave it. And then just save it. And now your codeex instance will be set up to prevent certain kinds of destructive commands from ever happening in the first place. So for me, this is a sufficient level of safety.

**55:30** · There are more complex types of safety that you can add using things like Docker sandboxes or simply working on your stuff on a computer which is totally isolated from anything else that could be damaging. So, it's your own decision of what you prefer. Maybe start off in default permissions, but I think that pretty soon you'll get annoyed and you'll want to move to full permissions.

**55:56** · In that case, I recommend setting up destructive command guard. And you can do that all within the Codex desktop app by opening up a terminal right there in that environment. All right, the next topic I want to discuss is the agents.m MD file. Now, if you recall back to a previous section, we were discussing how there are all these different things that use up tokens in codecs. One of those is the system prompt, which includes this thing called agents.md.

### AGENTS.md project instructions

**56:27** · So what is agents.mmd? The agents.md is a file that codeex reads before doing any work. And so the possibility or the promise of agents.md is that if there are certain types of things that you always want codeex to know about your project, you just create an agents.md

**56:49** · file, put it at the root location of your project folder and then codeex will always read that first before following any instruction that you give in any codeex thread. Now, there's not just one agents.mmd file, but actually multiple of them. So, typically at your individual project, you might put agents.md at the root of the project.

**57:14** · But, additionally, you could have an agents.md inside some folder in your project and then when codeex goes inside that folder, anytime it's acting in that folder, it'll always read that agents.md file first. And finally, you can also have an agents.mmd file which you put in your home directory in thecodeex folder.

**57:38** · And then this will be something that codeex always reads in every single one of your projects. So should you always make agents.md files, other AI influencers will sometimes refer to these as the brains of your project. But my opinion is that you actually should never make agents.md files.

**57:58** · The fundamental reason for this is that coding agents like codecs have gotten so good that you don't need to really tell them many things about what your project structure is and how to work inside it.

**58:14** · They can usually just infer that themselves. But what often happens is that if you put some set of instructions in your agents.mmd file if you're a beginner, you'll often overspecify things that aren't actually necessary to say, and so you'll just be using up valuable context in that agents.md file.

**58:33** · Additionally, if you have instructions explaining your project structure in the agents.m MD, but then down the road your project's structure changes, this inconsistency can end up confusing the coding agent, and so you get worse results than you otherwise would. To test exactly this, some researchers at a very prestigious university in Switzerland in Zurich did a test to see whether agents.md files actually help.

**59:02** · and they compared across some measure of success rate LLM generated agents.mmds, human generated agents.m MDs and no agents.m MDs. And what you see is that like for the worse models like GPT 5.1 Mini and Quen 330B, there does seem to be an improvement especially from creating this human generated agents.md.

**59:27** · But when you look at GPT 5.2, 2, which is now a pretty old model, or sonnet 4.5, which is extremely old. There's basically no difference at all. And so that speaks to the fact that as these models are becoming more intelligent, there's just less of a need for these agents.mmd files. And in fact, it can even end up hurting you. Here we have an other view studying the same thing.

**59:47** · But what we're looking at here is whether on these two benchmarks, whether using an agents.m MD helps you satisfy that benchmark with fewer steps and at a lower cost. And what you find uniformly across all these models is that these measures are done worse like in more steps and at a higher cost when you use an LLM generated agents.mmd or even a human generated agents.mmd.

**1:00:17** · Now, if you do create an agents.m MD, my recommendation is to put instructions based on what the agent is getting consistently wrong in your project. So, use the agents.m MD as a corrective. And so, for example, if your project uses one more modern library that may be past the models memory cutoff, then you want to specify that. So, for example, if you're using Tailwind version 4, specify that and not Tailwind version 3.

**1:00:49** · Or if you're using Python 3.14 specifically to write your code and you always want to make sure it uses that, then specify that. But the type of thing that would be bad to include in your agents.m MD is stuff like the database has 12 tables, the project structure is data, paper, intermediate, temp, because all of those things might change. certain types of things that people put in agents.mds actually belong in what are called skills.

**1:01:20** · And we're going to be getting to that in just a few sections. But before we get there, I want to introduce the five practical primitives of codecs.

### The five practical primitives

**1:01:31** · Now, when we were going over the interface store, I already gave you an brief introduction to each one of these, but I want to kind of lay a road map and make a brief comparison of these things right now so that you have a broad picture in your head as we go through each of these in detail. So, from your perspective, the way you'll be interacting with codecs is through this desktop app. And so under the hood, it's talking to your computer.

**1:02:00** · It's using command line interface programs on a terminal, but you don't have to actually touch the terminal. You could use codecs at the terminal if you wanted to, but the desktop app is a much nicer, much more comfortable interface for beginners.

**1:02:17** · But even for me as an experienced user who really likes a terminal, the Codeex desktop app has so many conveniences and utilities for power users like work trees that we're going to be getting into that really it's kind of the best environment for everybody to do agentic coding. And so inside codeex, there are these five things that you're going to be able to use to expand Codeex's abilities, the types of things that it can do. And so one of these is going to be plugins.

**1:02:47** · plugins are sort of builtin connections that Open AI and various companies have made to let you hook up to things like Gmail, Google Drive, Fathom, Linear, Figma, Notion, all these different programs that you may already be using and be able to talk to them from the Codeex desktop app itself by just clicking one button to install the plugin, an authentication flow, and then you've got access.

**1:03:14** · Now, one of the plugins that sort of deserves its own category is that of computer use, which allows you on a Mac, but soon to come on Windows as well, to actually control your entire user interface with codecs.

**1:03:32** · So, it can go and log in for you, look at your emails, download attachments, analyze them, all that kind of thing.

**1:03:42** · And all you have to do is enable this from within codecs. Now plugins and computer use set up these connections to these tools, but you may have much more particular workflows that you use that build on top of tools like Gmail, Google Drive or Notion. And so you may have a lot more particular needs. So for example, you may want to take your emails and classify them every single morning according to some heristic you like to use. So you want to find newsletters, summarize all of them.

**1:04:13** · You want to block spam. You want to flag some high priority people like your boss or your co-workers so that they come to the top of your attention and especially clients. And so ideally you'd like to have some kind of automation very particular to you and your workflows and your business and your needs. That's what skills enable you to do. And so we'll be going into skills in detail.

**1:04:40** · Now under the hood, what a plug-in is sort of doing is making a wrapper usually around what are called MCPS or model context protocol servers. So MCPs are a communication standard that has been established for different AI systems to be able to communicate with other systems.

**1:05:03** · And so sometimes a plugin may not already be available that connects to a particular system, but you'll still be able to connect to it if it has an MCP or an API, in which case you can build a skill. Now the distinction between skills and MCPs is often something that confuses beginners.

**1:05:26** · And so when I discuss MCPs, we'll be getting into that in detail. And finally, a last topic that we'll be covering of codeex's main capabilities is that of a sub agent. And so sometimes you're okay working in a single codeex thread, but other times, for example, if you're doing summaries of a dozen different PDFs, maybe it would be useful for codecs to be able to parallelize that task that you're doing.

**1:05:54** · And there are other kinds of situations that you might imagine wanting to be able to parallelize tasks with codecs. And sub agents are the tool that allow you to do that. just on call. You can basically spin up many different instances of codecs and have them attack some problem that can be broken up that way much more quickly and much more efficiently. So that's the last sort of final primitive that we'll be getting into.

**1:06:21** · Now the one of these five that I personally like the best and which I use the most are skills. And I think that once we get to that section, you're going to learn why.

### Plugins and the plugin directory

**1:06:32** · But the one that's really the easiest to use and will get you value right away.

**1:06:37** · And so which is why I'm going to be showing it to you first are plugins. So we're going to be starting to talk about plugins first. So to start, what exactly goes inside a plugin? Well, they're basically combinations of the following three. There's skills, which again we'll get into later. MCPs and apps, which are connections made from the chat GPT app itself. And so you might be saying, Anik, you haven't even explained to me what skills and MCPs are yet. How do I use plugins?

**1:07:10** · Well, it's actually quite easy. Let me show you how. So, if we come over here to the desktop app, you'll see on the top left an icon and a little label for plugins. So, let's click on that. And then immediately scrolling through here, you'll see a large series of plugins. So if you use Outlook, you can connect to your Outlook calendar directly from Codeex. You can connect to your Outlook email. If you want to build iOS apps, then there's a plugin to facilitate certain aspects of building an app.

**1:07:42** · So you can come here, click in on it, and you can see what this plugin includes. And so, as I was saying, there's an MCP server here, which is included, which helps you debug apps on simulators. And then there's a bunch of skills here as well for certain kinds of things which are useful to do in iOS, adopting modern iOS patterns. I actually haven't tried this out yet, and I'm building an iOS app, so I'm definitely going to try it out.

**1:08:12** · Let me show you a few more cool plugins. So, this one is for Remotion. If you haven't heard of Remotion, it's a React library that helps you create videos from code.

**1:08:23** · And so if you just install this plugin, this plugin just consists of a single skill, which for now you can just think of as a set of text instructions on how to apply Remotion for this programmatic video creation. So there's a few more cool plugins that I'm seeing here. So, first there's many for financial research to Morning Star, Moody's, and Dow Jones. And I think this one looks really cool.

**1:08:50** · There's a Read Wise plugin where if you're using Readwise to highlight different things in your Kindle or on the internet or whatever, you can use this plugin, which this one is just an app to search across all of your highlights, everything in your library, anything that you would want to do in Read Wise as possible. Now, the plugin which I want to show you and demonstrate here is the notion plugin.

**1:09:19** · So if you're not familiar with notion, it's a software which people use for a lot of personal knowledge management. So I have all sorts of different databases that I've put together. This is a database of local newsletters. I used to do some work in the local media space.

**1:09:35** · And so if I want to set up this connection to notion, all I have to do is come here and press add to codeex. So let me do that right now. Okay. Just going to say install. Great. It's installed. And so let's go here to try and chat. And you can see that when you click that button, this thing is already available, but let me get X out of it.

**1:09:58** · And you can see right here it says at to use plugins. We already covered that. So I'll go at notion. And let's say how many newsletters are in my local newsletter database in notion. And let me put this reasoning effort on Medium so it goes a little bit faster. All right. So we see that it's using notion thinking. I found a database titled newsletters database which looks like the target. The database has a single data source. So this is nice and clean.

**1:10:27** · I'm running a count now. All right. So this count thing didn't work because that's actually not available in notion.

**1:10:36** · All right. So this one is trying to work. It found the database, but it seems to be getting stuck and saying that it can't query more than 25 newsletters from the database. And so going back to these five capabilities, this is actually a useful instruction.

**1:10:52** · So these plugins are like connections to external systems. And this experience that I'm having right now with the notion plugin is probably something that you're likely to have too when you try to use plugins out of the hood because they're not super customized. And so they don't have all the cases for your particular workflows built in.

**1:11:13** · And so if I instead built a skill using the notion API, I'd be able to have something much more specific like an instruction that whenever you interact with a database, make sure you pass a pageionation parameter to go through all the results.

**1:11:33** · Or initially it was trying to use some kind of count query to count all the records in the database. And so instead, I would figure out what the right way is to do things and then just have that in the skill instruction that I created.

**1:11:48** · All right. Interesting. So it can't get the exact count. Can you look up whether the Catskill crew in Anapapolis, Maryland is in the database? Wow, I spelled database wrong. So let's see if at least it's able to find a record in Notion. Ah, so I actually made a mistake. This newsletter isn't in Annapolis. It's in the Cascills regions of New York. And it found the URL. So it's in there. Do you find anything from Annapolis?

**1:12:20** · And so let's see if it can do that. All right. So it didn't find anything for Annapapolis, Maryland. So let's see if we can add a record to the database. So I'm going to ask it, can you do a search for newsletters in Annapolis? I think there's one starting with Naptown. Look up its deets and add it. All right. So, it found a newsletter. It even found the owner on the internet. And now it's going to try to add that to notion.

**1:12:51** · So, that's pretty cool. It found his LinkedIn, his Twitter, the owner website, and it says I verified the new notion row exists here. So, let's go take a look. And yeah, we see it over here. And if we come back to this database, we see that the last record here now includes this newsletter. So the plugin is pretty handy.

**1:13:13** · There's maybe some things you can't depend on, but if out of the hood you're using notion databases, you want to be able to interact with them with codecs and apparently you don't care about counting, you just want to be able to add records and retrieve them, then this is going to work for you right out of the gate. And so as you go through here, I think that a lot of you are going to want to try out, for example, the Gmail, Google Calendar, and Google Drive plugins. And I recommend that because there's going to be immediate added value to having those integrated.

**1:13:46** · And there's a Slack plugin. Now, one question you might have is why don't I use these? You can see that I'm not using these right now, and in fact, I wasn't using the Notion one either. And that's because I've created my own more specific workflows using the notion API directly with the skills concept. So this is prefacing where we're going to go.

**1:14:07** · But if I search notion here, we see that in one of my projects for pay slice where I'm the director of AI and ML, I've created a kind of exhaustive set of SOPs for lots of different things we do for managing support cases, emails that come through and triage that we have to do all inside notion. So this is a much more specific set of instructions that I've developed and I have that for email, Slack, and Drive as well.

**1:14:34** · But if you don't want to figure out how to do that right now, you want to get started, have something useful to do, definitely use plugins. Now, something else worth saying is that you can build your own plugins, too. I consider this a kind of advanced feature that's outside the scope of this course, which I'm making for total beginners, but I do want you to be aware of this possibility. And additionally, you can install plugins that are created by third parties.

**1:15:03** · And so if you come in here, you can see that right now all the plugins available say built by open AI. And if you want to see plugins that are built by other people, you have to register what is called a marketplace. Now, we're going to be getting to this concept a little bit later because for app development workflows or just complex agentic workflows, there's a plugin here which I really like to use called compound engineering.

**1:15:35** · Now, this plugin used to be primarily for claw code, but recently they've made it feasible to use natively within codeex as well. So once we get to the part of the course where we're developing an application live, we're going to be using this plugin for this and that plugin has skills, it has sub agents and so all of this is going to come back and sort of congeal into one thing. You know, all this knowledge will be reinforced throughout the course.

**1:16:03** · All right, the next thing I want to teach you guys is about a particular plug-in called computer use. Everything Codeex has done so far has been inside your files and your terminal. Computer use flips that. Codeex actually opens up programs, reads what's on the screen, fills out forms, and clicks buttons itself. So instead of setting up a notion plugin like we just did, you could just use computer use to have codecs operate in notion itself.

### Computer use

**1:16:35** · Now, computer use is so important that if you look here in your settings menu, it's a plugin which has its own tab over here.

**1:16:47** · And so, if you want to use it, you come here to computer use. You can click on it. You'll have to go here and install it. And then you'll have to go through a set of permissions prompts to be able to let codeex computer use control things on your computer. But once you have it, you'll be able to give commands like this. Play a playlist to help me lock in. Okay, that's kind of trivial. Play a game in chess.app.

**1:17:12** · I guess if you want to play chess with codeex also may be useful, but more importantly is that you can give it prompts like this. Build and run my open Xcode project and test it for bugs. So, this is going to be a tool which once we get to the app development part of this course, you're going to be able to have Codeex try out the application you made and make sure it actually works like you think it would.

**1:17:39** · Now, unfortunately, computer use right now is only available on Mac, but Open AI has said that this feature will be coming to Windows as well. So, if you're on Windows, feel free to skip this, but eventually it's going to be useful to you. And for Mac users, definitely stick around. This is a very useful feature instead of staying at a theoretical level with computer use for a while. I think it's just going to be helpful to show you a practical kind of thing that computer use is able to do. So, I'm going to open this up. Say try in chat.

**1:18:12** · Let's work in my agentic config chat.

**1:18:15** · We're going to work locally. I'm going to say, can you go on X, look up my list of economists, and give me a summary of things they've tweeted in the last couple days I might find interesting.

**1:18:37** · Yeah. So, X has an API. It's a little bit expensive to use. And so something I'm curious here is codeex capable of doing a search or summary of content on Twitter without using the API because if that is possible then what I could do is make a set of profiles and later we're going to be getting into this but I would be able to use this computer use plugin to create an automation which makes a summary for me of tweets from economists that I find interesting.

**1:19:10** · And what you can see here is that this tool is able to navigate on Chrome. And you can actually see right there that it's actually looking at Chrome itself and it's doing this in the background without blocking the rest of what I'm doing. That's something really miraculous here that Open AI has been able to figure out and configure with computer use.

**1:19:35** · So I can go on and you know I'm working on some other things as well like this project here and I can keep working on this project while in the background codeex is doing an analysis of all these different economists tweets. So this is pretty incredible. Here we got in just a few minutes a complete set of summaries of all these tweets from all these economists that I follow.

**1:20:03** · And if I like click on one of these, it's going to take me right to that tweet. So that was actually a repost of something an economist. There's another repost.

**1:20:15** · Repost. Let's take a look at an actual post. Okay, good. So it is going to an actual post. And this is like a relatively recent post. And then it's got some small fun ones. I'm pretty happy with that. Now, what else could you use this for? Well, one of the things that I have to do at Pay Slice is I review session recordings like this one of users actually interacting with our application and I try to see places where there may be having bugs.

**1:20:45** · Now, that's a little bit timeconuming. It's not something that I always want to be doing and so something very nice is that I'm able to use computer use to automate that as well. And then I get bug reports directly that involve very detailed analyses of where certain user flows break down. And so this is a little bit forward thinking, but a lot of you may have aspirations of building applications yourself.

**1:21:16** · And computer use is going to be very useful for that.

**1:21:21** · I've also used computer use to set up my projects in Da Vinci Resolve when I'm trying to move certain files onto my timeline. And so I think that this is a direction that just AI is going to be moving in general, especially as the underlying vision models keep getting better. I put out a video recently on chat GBT's image model, which is absolutely incredible, and it's part of the reason why computer use is able to work so well in codecs.

**1:21:48** · Now, most of the time if there's a plugin available and you're a beginner and you don't want to make your own skill, which is coming up in the next section, then you can just use the plugin. But sometimes there are things that plugins won't enable you to do. And so computer use can be a way to get around them.

**1:22:07** · But let's say you wanted to have some kind of automated workflow, whether with computer use or with anything else. the one of the five primitives that I just told you about that you're going to want to use are skills. So, let's get into that topic.

### Skills deep dive

**1:22:24** · So, if you recall this figure, plugins and computer use, which we discussed right now, are kind of like one click and they get set up right away. And that's why I wanted to introduce them first because you'll be able to get immediate use out of them even without really knowing and understanding how skills work. But once you want to have very specific instructions for your particular workflows, skills are the tool that you're going to want to use.

**1:22:53** · So what are some types of example skills that I use myself? Let me show you. So if you come here to the plugins tab and then click on skills, you can see a set of skills that you can just install right away. So one new skill which Open AI has recently come out with is this image gen skill. So you can generate images inside codecs using the new chat GPT images 2.0 model.

**1:23:19** · A pretty common type of skill that I'll have are writing skills that convert from one format to another. So, I've gotten kind of bad about this, but for a lot of my videos, I'll have corresponding tutorials on my site, and I use this skill to take the transcript of YouTube videos and then turn that into a tutorial that shows up on my website. Now, that's not the kind of thing for which anybody's ever going to create a plug-in, but it's something that I can make with codeex myself to automate a manual workflow.

**1:23:51** · Here's an example from Pay Slice. We have a support email inbox where users can send in complaints and I have a support email skill that I've developed to handle the different kinds of cases that we have but then also create in our notion database a support ticket to make sure

**1:24:13** · that we're monitoring that and then also link to clarity which is that tool we can use to see user behavior to actually try to link the user's issue to something that they're actually experiencing in the application. And finally, here's a very simple one. I have a skill to interact with my WhatsApp. So, I use WhatsApp a lot for family and friends. And I can use this skill to interact with and search through all my WhatsApp messages. You can do this with iMessage as well, with Telegram, with Discord.

**1:24:45** · I have one for Slack that I use a lot and I find very useful. Now, what a skill is often described as is simply just a text file.

**1:24:56** · And that is a little bit deceiving because rather than thinking of it as a text file, you should think of it as a folder. What does that folder include?

**1:25:06** · Well, one, it has to always include this skill.md file. It has to have that name.

**1:25:13** · It has to have the MD extension. This is the standard that is developed in the agentic coding space. Then along with it that skill may come with scripts. So for my WhatsApp skill or that YouTube to tutorial skill, I have scripts that interact with my WhatsApp that interact with my database and the skill.md file teaches codecs how to use those scripts.

**1:25:40** · Next, sometimes you may have other outside reference documentation. An example of when you may have this is if you have some kind of front-end design skill to describe your design tastes or preferences. Maybe you would have images as references in the references folder or actually maybe you'd put them in the assets folder, but these are kind of funible. You can have whatever folder structure here you want. This is just a pretty common way to put it together.

**1:26:08** · And then finally in codeex itself, there's a concept here of an open AI.l file. This is kind of the least important aspect of skills, but it is some codec specific metadata that you can optionally add to a skill, which makes interacting with it in codecs a little bit better, a little bit smoother, as I'll explain in a few slides. Now, the most important part of that structure I told you is the skill.md.

**1:26:35** · And so, here's what a skill.md file typically looks like. So it starts with this mandatory section which has a front matter and so that front matter is a name and a description. So every skill has a name. I have a WhatsApp description and then the description tells codeex when this skill should be used and for what it should be used.

**1:27:01** · Then below that there's a set of instructions on the skill that codeex should follow. Now when you look at a skill in this skills view in the codeex desktop, this is basically what the name is. And then this right here is a description. And then this over here is a beautified version of the markdown body of the skill.

**1:27:23** · And so this is a skill that I use to take all my Fathom recordings and grab the transcripts and put them to a particular location on an external hard drive right here, which I can then use and have to always be able to look over all my Fathom recordings.

**1:27:41** · If you want to see it raw, you can go over here and click open. And now in this view in VS Code, you can now see the skill in its sort of raw text format. So, it's got that name and then it's got this description and then there's a skill file. And you can see here that it says use the bundled bun CLI. So, I have a bundled script that it uses to interact with Fathom. And then here it tells it you need to have these API keys available.

**1:28:12** · These are the different ways in which you may want to use it. Now, something you might be thinking when you're seeing this is, well, I'm not a programmer, so how will I ever be able to make these skills?

**1:28:24** · Well, I am a programmer, but I didn't program any of these skills by hand, any of the scripts that these skills use. I simply tell Codeex what I want and natural language instructions, and then it creates the skills for me. And so, I'm going to give you a demo of that a little bit later in this section. Now coming back to this slide, you may ask like why does it matter that a skill.md file is structured in this particular way? And why not just put all the references, the assets, and everything in like one single file?

**1:28:56** · Wouldn't that be simpler? Well, if you might remember, a big part of getting good results out of Agentic coding tools is being very particular about what sort of context you're giving them at particular times.

**1:29:11** · And so you don't want to give the tool information it doesn't need because then your context window will fill up. You'll hit the compaction point and you won't be able to work as effectively or if there's irrelevant information in there, it might get confused and not do what you want it to do. What skills allow you to do is use a concept called progressive disclosure. So when codeex boots up, it boots up the system prompt, the agents.m MD, and it boots up all the skills into its context.

**1:29:42** · But the only parts of the skill that enter into Codeex's context before you've done anything is this metadata. So the name and description. And that only costs about a 100 tokens, let's say, on average per skill, which let's say you have 50 skills. That's 5,000 tokens. And since our context window is like 260 270,000 tokens, that's not that bad.

**1:30:08** · So like that's not a horrible amount of context usage before you've even started doing anything. But the skill.md body might be a,000 tokens, 2,000 tokens, maybe even 5,000 tokens. And so if we loaded up every single skills body into the context, we would quickly hit our compaction point even before we hit a single message.

**1:30:36** · And so that's really what prompted the AI community to come up with this concept of a skill to have some way to allow Agentic coding tools to do these specialized tasks, but then also be able to protect the context window while you're doing it. Another important aspect of skills is where they actually live. And so not every skill is going to be available or you may even want available in every project.

**1:31:05** · So for example that skill that I use to convert YouTube videos into tutorials I have installed at the level of a particular project or repository. And so the place that it needs to be located in the project structure is in this agents directory and then at the skills subdirectory in that particular project.

**1:31:32** · Next there are user skills and so the user skills are skills that you want to have available across all projects.

**1:31:40** · WhatsApp for me is one of those that you know from any project in any directory I may at some point just want to check in on my WhatsApp messages and so you would put that at your tilda which is your home directory in the same aagents/skills directory and then finally there are

**1:32:02** · system skills so these are skills that come bundled with codecs and are just always available you don't manage these but you should still beware aware that they exist because you're going to use them, especially these two, skill creator and skill installer. Now, as I'd mentioned before, there's a set of skills that you can install just by clicking a button and then installing a skill.

**1:32:24** · And then once you've done that, once you have skills available, either through this codeex UI or by installing them from the internet, I'll show you how to do that. How do you actually use the skills? First in this composer you can just put in a dollar sign and then all the skills that are available to you either in the particular project that you're in right now or your set of personal skills or system skills will all show up here.

**1:32:53** · And so you can see that there's five total system skills here. And we're going to be talking about a fair number of those. And so if I go like this and then I type in back test, I've now invoked that skill and then like whatever instructions I say are going to be interpreted in the context of that skill. But additionally, as I mentioned, for all of these skills, the name and description are loaded into Codeex's context.

**1:33:20** · And so if you simply type something in and codeex is able to infer that like that particular skill is what we should be using in this situation, it will autonomously decide without you needing to specify the skill specifically to use that skill.

**1:33:37** · If whatever you're doing seems to match that workflow, it's not a guarantee that codecs will act at a particular moment and you can have skills that conflict or it may not be super obvious when to use one or the other. And so that's somewhere where iterating on your name and really the description can help out quite a bit. Now, what skills are often doing under the hood is they're just helping codecs understand how to operate some script and make it useful for you.

**1:34:10** · So, let me show you an example of doing exactly that. So, this right here is a tool called YTDLP.

**1:34:19** · You can use it to interact programmatically with YouTube and a lot of other websites from which you want to download YouTube videos. And so, I like it quite a lot. I use it for doing research against YouTube. I mean, YouTube does have this Gemini summarize feature, but oftentimes what I want to do is a lot more custom. And so, what I want to do now is create a skill that starts with YouTube, but then we'll do something fun.

**1:34:47** · Now, if you want to create a skill, the right tool to use here is the skill creator skill, which comes with codeex. And so the first thing I'm going to say is that I want to create a skill in this repo because as you remember there are different scopes for skills and so I want this skill to be available just to this project. But in order to do make this skill it's going to require access to this tool YTDLP.

**1:35:14** · And so my recommended way for you to install this is using a tool called homebrew. If you've never used homebrew before I want you to go to brew.sh sh and then copy this right here. Then come back to codeex and then type in command J. And that's going to open up a terminal like this. Then you simply paste that command that you just copied.

**1:35:43** · Press enter. It might ask you for your password. You put it in and then let it install this tool. So, Homebrew is a very handy tool to be able to easily install a lot of useful packages that Codeex can then use. Once it's done, I want you to copy this that says brew install YTDLP and then back here in the terminal, just paste that in. Press install and it'll go through an installation process. That's basically the only reason why I'm going to need you to use the terminal in this course.

**1:36:16** · In the Clawed Code course, I was a lot more terminalheavy because when I made that course, the Cloud Code desktop app was pretty bad. It's since improved. So, if I was remaking that course, I wouldn't have focused on the terminal so much and just stayed in the desktop app.

**1:36:31** · But lucky you guys, you don't have to learn about the terminal, you can stay pretty much entirely inside the app except when we're just installing a few useful utilities like that one. So, we're back here. I want to create a skill in this repo. It should use YTDLP.

**1:36:48** · I want it to combine with image gen by downloading the transcript of the video and creating a very detailed infographic of the video. something pedagogical slashexpository.

**1:37:15** · So what I want to see here is can we combine a few things together? I want to make a skill. The purpose of this skill is to create some kind of visualization which helps me visualize what's in a video. And so if you've got a codec subscription, you have access to this new utility to do image generation. I made a video here that like nobody cared about about this, but it really was mind-blowing to me. I made this thumbnail here with this new feature.

**1:37:44** · Oh, yeah, and one other thing. You might notice here that now the UI looks a little bit different. It says 5.5 extra high. That's because just I'm recording this over multiple days and now the 5.5 model is out. So, that's the one I recommend you guys use. So, it already decided what it's going to call the skill. It's going to call it YouTube infographic. If you had a specific name that you wanted to give it, it would do that. So, let's just see how this goes.

**1:38:11** · All right. So, it worked for 6 minutes and it's created the skill. So, let's take a look at the skill itself. If you click on it, it's going to open up here.

**1:38:20** · And let's make this big so that you can see the whole thing. Is there any way to do word rap? I guess not yet. It's coming along, right? So we got the name, description, download YouTube videos, metadata and transcripts with YTDLP and a handoff to this image gen skill. So this is important to know that like skills can kind of chain together and that's what I'm demonstrating here. Then it's got you know like uh some instructions prefer human subtitles when available etc. And it also created a reference like infographic brief I guess of how to create infographics.

**1:38:52** · So let's take a look at that. use this reference after fetching transcript.md and before invoking image genen extract these items from the transcript. So let's just look for a video that maybe I would want done this way and then just try it out. So we're here on YouTube uh the original technobiking video. That's you know well set. I spent my entire life trying to be smart but I'm Let's do that.

**1:39:23** · That sounds exactly like the kind of thing that I would want to create an infographic about. Let's try it with this video. Make it funny. All right, let's see how it works. All right, so this is interesting. Created an infographic brief. Can we look at that?

**1:39:43** · General self-improvement audience. It can handle a loud comic motivational style. Use a comedic operations map poster. The anti-overthinking field manual teaching units verbatim labels for image. Yeah, let's see how it goes. I guess an important note here is that he's kind of edgy.

**1:40:07** · Founder of Andre Horowitz tweets about this guy a lot. I like him too. He's funny, but he does say the R word and you're not supposed to say that. So GPT will not let you include those kinds of word cruelty I guess fake statistics and decorative only imagery FYI. All right is done. Check that out.

**1:40:26** · So, one thing I'll say is that this like is kind of like funny in a cheesy way or I don't really think it's that funny, but for the purposes of creating this skill, especially if we were making it on like more serious topics like a visualization of some machine learning topic or you could even try it out on my own videos.

**1:40:51** · Maybe that's what I should have tried out instead. It's pretty good. Like, it's pretty freaking good. Now, this is kind of coming up in an unfortunately displayed way, but if you look here in the file viewer, you'll see that there's an agents directory as well in which there's something called openai.yaml.

**1:41:10** · This is sort of the optional thing that Codeex will create when it creates this skill creator skill that goes along with your skill. So, what is this exactly?

**1:41:20** · It's basically a set of instructions to give a little bit of extra UI polish specifically in the codeex app. So if you don't have this and the skill shows as its folder name only. And so for example, one of the things here that's included is this thing that says display name Figma. And so when I type in dollar sign, you'll see that these are all showing up in like a regular capital case, right?

**1:41:49** · And that's because there's these open ai.yammo files in the skill directly that is teaching, you know, how to format things. You can also decide if you want to be really hardcore to have little icons that go along with your skills. And over here you can have a sort of default prompt that is initiated whenever you use a particular skill. So this is optional and it's something that the skill creator skill will make for you itself.

**1:42:21** · But something to be aware of if you see this thing showing up in your directory and you don't really know what it is. Now I showed you how to make skills, but what if you just want to use a skill that somebody else has on the internet? And first of all, how do you even find other skills in the first place? Well, unfortunately, but actually it's not that big of a deal, but unfortunately, there isn't like some central repository of all skills. As you see, like these things are pretty easy to make.

**1:42:50** · You can just kind of tell Codeex your intent and then get the skill out. So, when skills first came out, there were people making a racket trying to sell skills. I think that's really stupid. There's very few people from whom I would buy their skills. Most of the people who are trying to sell you skills are just taking advantage of your lack of knowledge about this space. So now you know you can pretty much make your own skills for anything you would ever want. And so me personally, I just make pretty much all of my skills.

**1:43:22** · I almost never look for is there a skill available to do something I want to do.

**1:43:30** · I just make my own skills because it really is as easy as what I just described. You can iterate on it and there are more advanced ways to think about the construction of skills, but for most of what you guys want to do, you can make a skill almost exactly just like how I described. Now, if you do want to find some skills, I would mostly just Google or perhaps look on Twitter for like skill for notion or something like that.

**1:43:54** · And then if you find a skill, let's say it's on a GitHub repo or in some web page which has an index of a lot of skills, here's how you would install it. So coming back here, if you just type in skill, you'll see that there's skill creator, but there's also skill installer. And so let me find some skill and then just show you me installing it and then using it. So this right here is Anthropic's front-end design skill.

**1:44:21** · It's a skill that you can use and it consists literally of a single file, nothing else to create front-end interfaces that don't seem generic. And so in the past, I found Anthropic to be or rather claw to be a lot better at design, especially when you combined it with a skill like this.

**1:44:41** · Now, I actually find codeex to be my preferred choice for design. Little bit outside the scope of this video, but something you guys can be aware of.

**1:44:48** · Anyway, part of the types of instructions it gives here is to help cloud code or codeex or whatever tool is using these skills to avoid certain kinds of things that AI tools tend to do when they're creating interfaces. And so, let's copy that and say, can you install this skill just in this repo?

**1:45:10** · Enter. So, you found a skill, you want to install it. This is how you would go about installing the skill. You can ask codeex to either install things in a particular repo or at the user level. I don't want to corrupt my other interfaces. So I'm going to get it installed just in this repo. And so you can see the installer expects a skill directly. All right. So the skill was installed. It says restart codeex to pick up new skills. So if I go front end design, I'm seeing this because it's part of another plugin that I use.

**1:45:41** · All right. So I restarted. Now, let's go front end. Hm. It's not showing up. All right. So, something to be aware of is that it installed it in the wrong location a few times. So, first it put it in this skills directory. Didn't show up and I was like, why isn't this happening? But then I forgot this has happened before. Then it put it in theclaw directory. And then finally I told it, no, it has to be in agents. So, I put it there and now it shows up.

**1:46:08** · And so I can say uh make me a pretty website about that YouTube video. Make it in the theme of notion just a single HTML page and then boot it up in the in browser.

**1:46:31** · So, let's see if we can use this skill now that we installed to make an example website about the same YouTube video and see what comes out. All right, here it is. So, haven't told you guys this yet, I think, but Codeex has an inapp web browser which is very useful to use when developing a video. And you can see here that this is like a pretty neat website that it's made. It's notion themed.

**1:46:59** · Even included that image that we just created all in this website. So you can really expand the set of possibilities here once you just make a little bit of progress at understanding how these tools work. And you can see right now it's actually using computer use. So it's sort of combating with me to take a look at this website and see if it looks formatted properly. And so now it's finding, you know, some mistakes in the formatting here, I guess.

**1:47:29** · And this thing over here is codeex's or rather computer uses, I think, cursor. So anyway, I'm going to stop it right there. But I'm pretty happy with these results. One last practical thing. If you come here to plugins and then go to skills, if you decide you want to keep a skill, but you don't want it to be activated to show up right now for whatever reason, you can just go over here, click this button, and then you can disable the skill for the time being.

**1:47:58** · So, if you have tons of skills, like you shouldn't have this, but I I have a ridiculous number of skills, right? And so maybe I would actually either be concerned about them eating up the context window or there could be some situation where like certain skills seem to be interfering with others. So I just want to temporarily shut it off. That's something you can do in the codeex desktop app. So coming back to this chart, right? We've discussed plugins and computer use and then we discussed skills.

### Skills vs MCPs

**1:48:25** · And what we described the plug-in as sort of being under the hood is a skill plus sometimes an app connection. And then also this third thing called an MCP or the model context protocol. So that begs a question, what are MCPS and what are they useful for?

**1:48:46** · All right. So, we've now installed and built some of our own skills. And my general opinion is that by default, when you want codecs to interact with some external system, skills are going to be your go-to tool, but they're not the only one. And so, we're going to get to the next one now, which are MCPS or model context protocol servers. So, as the documentation here specifies, MCPs are an open- source standard for connecting AI applications to external systems.

**1:49:17** · And the right way and like a common analogy that's used to think of them is to think of them as a USBC port for AI applications. So, what does that mean? It means that in the past, every AI application would develop its own standard for how your AI should connect to it.

**1:49:36** · And MCP has been established as one official standard that everybody uses so that anytime your AI wants to connect to external systems, it knows the general method of doing so, which is MCP. And so under the hood, this MCP specification is this technical specification where the server is defined by a big JSON file in which particular tools are made available to you.

**1:50:07** · Now you may not know it, but in this course you've already been exposed to MCPs. And the reason for that is that most plugins in codecs are actually using MCP under the hood. So let me show that to you. So here's the notion plugin. And as you see, the notion plugin includes this app. And under the hood, this app is just an MCP.

**1:50:29** · And so this app contains different tools such as notion create comment, notion create database, notion create pages, and then there's a set of instructions for the AI system codeex in this case to help it understand how to use this tool. Now under the hood, both MCPS and skills are working with some APIs.

**1:50:57** · So if you make a notion skill, it has to interact with this API directly. And if you want to use an MCP under the hood, it's often or pretty much always just sitting on top of an API. And so when the AI is taught how to call these tools, these tools themselves are just formatting some kind of request of an API.

**1:51:24** · Generally, my advice is that if you have the option of attaching to the same service either by an MCP or a skill, if you plan or expect to customize your use of it, what you should do is pretty much always make a skill.

**1:51:44** · Now that skill you can choose to either hit the API directly which the MCP is hitting under the hood or you can have the skill actually have your own particular workflows that are built around these different MCP tools. Now sometimes an application may not give you direct access to an API and so in

**1:52:09** · this case your only way to interact with the external system since you're not going to be able to make your own skill which uses their API is going to be using their MCP if that's what they're making available. And so, for example, here in the AI MBA Pro, every single time we have a call, the call comes up here, but then if you click in on a call, you can go back to the call, but also see the full transcript here.

**1:52:36** · And what I've chosen to do is make that transcript available to AIMBA Pro members by MCP. And the reason I've done that is because it's easier for me as the application developer to serve a broad audience who may all want to do their own different things with the transcript by just making all the different resources that I provide to pro members whether courses, tutorials or call transcripts available by MCP.

**1:53:12** · And so you can see here that I give agents access to four different tools where they can list the pro resources, search across them, get some pro resource, and if a pro resource is really long, like a transcript, then they can get it in chunks. And so I actually give detailed instructions here on exactly how to set up an MCP in the Codeex desktop app.

**1:53:38** · So let's try following those instructions and we'll be able to use that to understand what value this gives us. So you go up here to codeex then to settings and then over here you'll see MCP servers. So let me click on that. And now I already have some MCP servers connected. If I want to enable or disable them the ones that are already connected I can use this toggle.

**1:54:03** · But here I'm going to say add MCP server. And you're going to see that there's two different options, stdio and streamable HTTP which are available.

**1:54:15** · So the main difference between these two is that this one stdio the MCP server actually lives and is hosted as a service on a port typically on your own computer. Whereas with streamable HTTP, some other service like on the external web is hosting the MCP server. So most places are now going to have you go through this option because it's a lot easier for users.

**1:54:41** · And then you may get instructions to fill out some of these fields depending on how the authentication process works to be able to use the MCP. So, I'm just going to go ahead and register with AIM MBA Pro. And then back here in the instructions, this is the URL for the MCP. So, I'm going to copy that. And then I'll just click save. So, if it's your first time using an MCP, what you might see come up here is a prompt to authenticate.

**1:55:12** · I think since I had already registered this MCP in the past, perhaps it's not giving me that prompt. But if you get that, you'll just have to press authenticate. It'll open a browser window where you'll log in, perhaps go through some permission systems and then you'll have access to the MCP. So, let's come back here to the app and I'll open up a new chat. All right. So, I'm here in the app now and if you go back/mcp, you can see the status of your different MCP servers.

**1:55:42** · So, we see here that I'm already authenticated with OOTH to AI MBA Pro. also authenticated to this one.

**1:55:52** · For some other ones, it says O unsupported. And so what I'm going to ask now is use the AIM MBA Pro MCP to summarize the last AI MBA Pro call as if I am a Pikachu. And let's see how it does. So it seems to be aware of the MCP using AIMBA Pro searching pro resources.

**1:56:19** · Okay, it found the latest call. I'm grabbing the resource details and a transcript slice. So, the summary has teeth, not just title level sparks. And so, it's grabbing different chunks of the transcript. And now, it's got a pretty comprehensive summary of the call.

**1:56:36** · And so what I'm going to ask it now is, can you give me exact timestamps and exact quotes from the call for each of these points because what I want to see is if it's just picking up the summary on the site or if it's able to get exact details in there. Hold on. The call transcript. No, it's my own call, dummy. That's pretty interesting.

**1:57:02** · So sometimes, you know, the codeex model will just be extremely annoying like that. Yeah. And so that's pretty cool.

**1:57:12** · It's able to get, you know, like exact timestamps based on this MCP and exact quotes. So all the AI MBA Pro members can use this MCP server to access all the tutorials, all the different courses that I'm putting in there, and then of course our weekly call transcripts.

**1:57:30** · Now, if you wanted to have your own personalized summary as a Pokemon trainer or just as a person who owns a particular kind of business of the calls, then what you would want to do is create a skill which builds on top of the MCP with your own particular workflow. So, this is a good example of how skills and MCPs can work together.

**1:57:55** · But from your perspective, most of the time you're going to be good with just plugins and skills, which I've already introduced. And sometimes you will have to work with MCPs which is why I wanted you to at least be lightly aware of the topic. Coming back now to these primitive capabilities, we've covered plugins, computer use, skills, and MCPs.

### Subagents

**1:58:18** · And so the last one we have is how you parallelize work in codecs and that is sub aents. Sub aents are parallel instances of codecs. So typically when you're here in codeex you're working in a particular thread. This thread has its own context window and when you reach your context limit codeex is going to go through this compaction process.

**1:58:42** · Now, what a sub agent allows you to do is to spin up other independent instances of codecs and send to them different types of work that you may want them to do and simply have them come back and report that work to the main thread. And so ordinarily, for example, all of this work may involve going through one or two compaction events.

**1:59:11** · But maybe you don't actually care for the main work that you're doing about all the internals of whatever goes on in a codebase exploration. All you care about is about the final result of a codebase exploration as it applies to you. And so in this situation, it may be appropriate to invoke a sub agent to parallelize your work.

**1:59:38** · Some of you may be familiar with sub aents in claude code and you'll see in claw code claude code spinning up sub aents of its own accord. Codeex doesn't work like that. You have to explicitly tell it when you want sub aents to be invoked. And so when should you invoke sub aents? I think generally a good but not perfect heristic is when whatever it is that you're tackling is a clearly divisible task versus a fuzzy task.

**2:00:11** · And so things like figure out the strategy, fix the app, improve the workflow. To be honest, these are just generally bad instructions. But for example, let's say you're doing a code review on a code base which has many different modules. It's an unfamiliar codebase to you. Something that might make sense is for you to have codeex go and deploy a sub agent to inspect every single module and come back to you with a report of how it works.

**2:00:39** · Instead of there are six or seven code modules that you need to understand, you can speed up this process with a divide and conquer with sub aents. Codeex does come with some builtin sub aents. These are a default general purpose agent, a worker sort of execution focused agent for bounded code docs or test changes and an explorer agent for read heavy codebase type questions.

**2:01:09** · In practice, when you're working with sub aents, you don't have to remember these distinctions between the built-in sub aents because based on the task to which you are applying sub aents, codeex will choose the one of these three or the combination of a couple of them which makes the most sense for whatever your application is.

**2:01:31** · Now when you have some task that you repeat often, you can create your own custom sub agents to be able to use them in a repeatable way. So for example, here's a docs reviewer sub aent which reviews docs for accuracy and missing steps. And here's a set of developer instructions that are given to it. And so these three fields name, description, and developer instructions are required when you're working with sub aents with codecs.

**2:02:01** · There are also other optional fields such as nickname candidates, model, model reasoning effort, so you should be familiar with these sandbox mode, MCP servers, all things that you've already learned about. And skills config to know what kind of skills for that sub agent to have access to. And so again, just to kind of emphasize the point, if you're working on parallel codebase research, great place to use sub aents.

**2:02:29** · If you have independent documentation updates across many different parts of your documentation, another great place to use sub aents and I want to even say while implementation continues, but just for code review in general, a very nice trick is to define sub aents each of which are dedicated to studying a particular aspect of your code and reviewing it.

**2:02:55** · So you may want to have one which is focused on security, one which is focused on architecture and another one which is focused on the efficiency of your database queries. That would be a great place in which to use sub aents. Now just like with skills, if you want to use these custom sub aents, you need to put them in your.codeex/ aents directory instead of your.codeex/skills directory.

**2:03:25** · And they have to have a particular format called a toml format.

**2:03:31** · TOML files look like this. And so here for example is a toml file for a python code reviewer sub aent. So I can zoom in a bit and you can see it's saying prioritize smallest safe changes that preserve established architecture quality checks etc. And so these kinds of things may be useful for you.

**2:03:53** · Now as a practical exercise using these sub aents I wanted to try to use sub aents to understand a code base which I find very interesting and that's the code base of the pi coding agent. So if you're not familiar with pi it's a minimal coding agent just like codeex and claw coder coding agents which has been created by a fellow named Mario Zechner and I've heard lots of great things about it.

**2:04:21** · I want to start experimenting with it and also build my own agents which build on top of it. So it's something I've been interested in understanding in more detail for a long time. And as you can see here, it's consists of about six different packages. So if I'm coming to this with no understanding of the repo, this is the type of situation for which sub aents are really appropriate and are exactly the kind of thing that you want to use.

**2:04:52** · And so let me show you exactly how I would do this. I'm just going to copy this and I'll come back to codeex.

**2:04:59** · Let me just open a new thread here. I'll paste this in and I'll say clone this out to temp. Then I want you to invoke sub agents each of whose purpose is to create an educational HTML file which helps me understand the basic idea of each module in this repo.

**2:05:26** · I think there's like six or seven packages and how they relate to the other ones. But each sub agent should be primarily focused on its own package.

**2:05:36** · And I know that there's a limit on how many sub agents you can use at once. So I want you to just choose the six or so most important packages to focus on. And so let's see how this goes. All right.

**2:05:50** · So we can see here that six agents have been spawn. And when the agents are spawned, they get these like funky names I guess of mathematicians. But I see all sorts of other ones. So we've got Russell, Bertrren, Russell, Pascal, Wagner, Uklid, Galileo, Ramuna, John, and they've each been given like a set of instructions. You are working in this directory. You are not alone in the codebase. Other agents may write files.

**2:06:19** · So only focus on this. And so it says these package agents are now running on these disjoint files. And so if we wait a few minutes, we'll get some response back and we'll be able to see what codec produced. Now, one thing to keep in mind is that when you're using these sub aents, it's true that they're not like affecting your current context, but they are going to affect your usage. And so, one of the reasons why Codeex doesn't tend to spawn up sub agents on its own is that if it did, that would really eat up your usage really quickly.

**2:06:48** · And so, you want to use sub agents when they're appropriate. Don't shy away from them because they can really speed up how quickly you're able to do some things.

**2:06:59** · But it is something to be aware of that heavy use of sub agents in general will use up your usage more quickly. All right. So sometimes some sub agents will finish earlier than others. So you can see that like some of these finished earlier and it's still waiting for these other three. All right, it finished. So let's check it out. Not sure if I showed you guys this feature, but you can open up stuff like in browsers directly here in the UI. Actually, I did show it to you when we made that website. So we got a guided index for understanding how they all fit together.

**2:07:30** · The onesreen mental model. Okay. It says read these six first. So let's start with this one.

**2:07:40** · Pi AI. I mean this is a pretty cool way to sort of get an overview of some package before you even start reading it. So you see it tells me the purpose gives me like a good mental model for the code base. tells me some key files to look at the data and control flow and then it even gives me this like code reading path to understand things in a particular order.

**2:08:06** · And so this is exactly what I'm going to do when I want to understand this package in better detail. And in fact, if you're studying some unfamiliar codebase for the first time, this is a really good way to get up to speed. So we've now been through all of these five capabilities. So you got plugins, computer use, skills, MCPs, and sub Asians. And if you're anything like me, I would probably feel overwhelmed if this was my first time going through all of this material.

**2:08:34** · It all kind of, you know, sometimes you understand a little bit, but then you forget some things. So, you know, feel free to go back through the course a few times, like pause, bookmark different sections. But what I want to do now is just give you a final broad overview of all of these tools and when to use one versus the other. So broadly here, often times what's appropriate to do is just to use a packaged capability. So you can use these plugins.

### When to use which tool

**2:09:03** · In fact, that's what I recommend to you guys if you're getting started with codecs is just come to this plugins page, find something that looks useful, press plus, try to use it, and immediately get really great payoffs by being able to connect codeex directly to external systems. Now, once you've been using codecs for, let's say, a few days, or if you just want to get started earlier, the next thing I want you to go to is skills.

**2:09:31** · And so skills are going to be using APIs, but they're really the most important thing that you could keep focusing on. I have a lot that I could say about skills past what I've said in the course. I probably have 100, 150, 200 different skills across all my projects. Some which I use on every project, most of which I only use on particular projects. And so in general skills are the one that I would recommend you focus on after plugins.

**2:10:06** · Now sometimes skills may not be able to do everything or and so for example it's going to be very hard to have a skill which connects to your Spotify and then starts a playlist. That kind of thing or just anything where you need real browser or app control, you're going to want to use computer use. And so I like using computer use all the time.

**2:10:28** · For example, like here I'm working on developing a mobile app and I have computer use come in and actually interact with this mobile app and see if things work properly. And so for that kind of thing, computer use is quite helpful.

**2:10:43** · Now, this is a little bit of a misleading thing because when you need reliable external access, you can get that via a skill, but sometimes the API isn't available to you, like on the AI MBA Pro, because it's easier for me to just serve an MCP because those can be used immediately by people without really needing any additional setup. And so, they're very similar to plugins. In fact, plugins are often just built on top of MCPs.

**2:11:13** · And finally, when in any of this stuff, like in a skill or sometimes even within plugins, you might package in sub agents because they help you parallelize things, but most of the time you yourself just when you see an opportunity to do things in parallel, it's a good opportunity to use a sub agent.

**2:11:34** · Now an open question which we still haven't answered and which is going to kind of guide the direction of the rest of the course is when would you want to build a full web application or a mobile application and when might you best be served by instead just making a skill.

**2:11:56** · Now obviously if you're serving clients and those clients want you to make a web app or you need to have a website something to present to the public you can't tell people oh hey have my skill and then you can use this API to connect via claude to my database and you'll know all about me right you need a website but in some situations it's not so obvious for a particular automation that you want to create whether you should be creating a skill versus an app. So let me get into that a little bit.

**2:12:26** · So generally if you're okay with just getting text output as the deliverable of some kind of automation then a skill is enough. Now if you want some kind of regular visual review or some sort of visual interface in which to see the status of some application on a regular basis and you need to be able to access this from any location. then maybe you might need an app because it needs to live somewhere publicly.

**2:12:57** · If you just need visual review, then as you saw, we can just spin up HTML locally, look at it like I did for that coding agent review, and that might work for you. So, this over here is not totally accurate because you can have state, meaning where you were at with a particular application, like seeing your last email that was reviewed, you can have that live locally on your computer as well.

**2:13:24** · But if you need to collaborate with non-technical stakeholders, they're not going to be able to work with skills, at least yet until you train them. And so, maybe an app is going to be the best thing for you to create with codecs for whatever it is that you want to do. And so as an example to sort of think through this and which is going to be the web app which I'm going to make with codeex live here. Imagine that you'd create social media content and you wanted to be able to automate the creation of social media carousels.

**2:13:55** · Okay. So these are some sort of web UI in which you're creating a image for social media. The optimal interface in which to work with this may require some visual judgment. fiddling things around, marking a particular social media asset as being done or not. And you can do that all with a skill, but often you're working on a team where everybody needs to be able to interact with this interface.

**2:14:22** · And so this might be the kind of thing for which you would want to develop an app which has a canvas, which lives somewhere on the internet, which can store your brand kit and have drafts. And so this could very well live as a skill if you're working on it on your own, but with non-technical stakeholders, you'll definitely want to have this as a web app. Now, another common pattern, which honestly I think will be the one we end up implementing is to combine skills with apps. And so, for example, notion is an app.

**2:14:52** · And if you build a skill on top of it, now you're combining skills and apps. And so similarly even with an app you build you might realize that the optimal workflow for like technical and non-technical stakeholders to work together is to create some kind of app with a skill. So one could imagine that you have some kind of command line interface which works with your database and then that results in things changing on your web app which is publicly available to everybody.

**2:15:23** · Allows a human to then review what's happening on the web app. But it's some skill interacting via a command line interface with the database which is designating what kinds of text come up on the social media asset, what sorts of images are included on the social media asset, that kind of thing.

**2:15:44** · Now, it may seem that creating this kind of web app is like mindblowingly difficult. And I'm going to show you in the rest of this course that it's not.

**2:15:53** · You have to understand some things architecturally, and I'm going to help you through them. But you can kind of backfill knowledge over time and mostly rely on the intelligence of these models and these tools to help you build even quite complex applications. Now, one final thing I want to mention just to preface where we're going is that some sorts of things you may want to set up as automations. They're actually quite simple to set up.

**2:16:19** · For example, you may want some kind of social media asset created in your application on a regular basis using some external data that gets loaded or using some kind of search to find information on the internet, grab it and then use that to create different kinds of social media assets, let's say for a news outlet. And to do that, the appropriate tool that codeex has for us is automations.

**2:16:47** · So, I'll show you in a later section how to use these automations. But especially as we move out of doing stuff just by ourselves, building our own little skills, working on our own projects, and having to serve other people. Something that you're going to have to get familiar with is how to keep track of your work and keep track of different versions of your work in a typical software development life cycle.

### Git and GitHub basics

**2:17:16** · And so the tool that we use to do this is called Git and GitHub which you've already encountered many times.

**2:17:26** · Now Git and GitHub may seem very complex especially if you've ever tried to use Git manually on your own, but coding agents are able to do a lot of the heavy lifting now. And so using both of these tools is way easier than it was in the past. But it is still extremely important to understand these tools conceptually because they're going to be very important for creating any kind of web app. It's impossible to do so otherwise.

**2:17:54** · But also to learn how to start doing not just creating sub agents to do tasks in parallel, but to work on different aspects of a project in parallel. So that's what we're going to get to next. So what is git exactly?

**2:18:11** · Well, typically when somebody new to computer programming or who is just typically working on word documents or whatever project, they'll make a change to a file and then they'll save it. And sometimes those applications will give you a way of going back to previous versions, but it's not perfect. You can't go back to every single previous version. You often can't see the exact difference in whatever files you made between one save versus another save.

**2:18:42** · Git is a perfect interface for computers and also for humans to be able to see the exact set of changes made at every point in time to every file. So you're able to see a summary of every change which is created by you. You decide in this summary what to put in here or in the new era the coding agent is deciding what to put in the summary. But you can also see line by line for each file what change was made at every stage.

**2:19:12** · And this is really important if you're working on anything involving code because you want to know, for example, if some bug has been introduced and you catch it a fair while on, what exact change in the code it was that introduced this bug. It also gives coding agents memory.

**2:19:33** · So they're able to see what you were working on, what the most recent files are that you've been working on in a project, which ones are older files, because the date modified of a file, especially if you're copying and pasting things around or moving from one computer to another, is not a reliable indicator of the history of a project. But the Git repository can be that very reliable history of a project, which is very informative for coding agents.

**2:20:01** · Now, one of the fundamental terms that you'll have to be familiar with is that of a commit. Committing is kind of like saving is what I was describing before.

**2:20:14** · Each of these right here are commits. In a commit, you declare what was done by git and then git tracks under the hood the set of changes that has been done in a commit. And so one of the plugins that I keep referencing and which we're going to be talking about is this compound engineering plugin. And you can see here that the compound engineering plug-in has had 734 commits. So let's click on that. And so we see here a set of commits that has been created.

**2:20:45** · And so let's take a look at one of them. And then here we can see the commit message which says restate model override at dispatch point. And we can see in this viewer in GitHub which I'll explain later exactly what the exact changes were that were made on particular lines in different files. And so especially when you're working collaboratively you want to see exactly what somebody has done.

**2:21:14** · This kind of interface and this technology makes collaborating much easier. All right, what I want to get started on now is creating this web app in git just the beginnings of it to show you how git works in a practical way inside codeex even without having much theoretical understanding and what you're going to see is that you don't need a lot of theoretical understanding to get started with git. Now, just as context, I used to do a lot of consulting and product building in the local media space.

**2:21:46** · If you look at a lot of my old content, I have this video here on how to automate a local newsletter with claw code, for example. And I was featured in this article from Neiman Labs about this concept of local newsletters where individual entrepreneurs are sort of creating local media outlets in their particular areas. And so here's one from a friend of mine, Jast Singh. It's very successful.

**2:22:13** · And you'll see that he's got like this kind of social media content, these carousels, like 10 Winnipeg events to add to your calendar this week. And so what I want to do with this web app is see if I can automate the creation of these kinds of carousels. And so I'm going to go here. I'm going to say create start from scratch. Or actually, let me how to create an existing folder.

**2:22:38** · I'll come here to projects. I'll say uh carousel automation app create open. Okay, great. Let me remove that one. And now I'm just going to describe this project that I'm going to make to codeex. So let's actually use this voice input.

**2:22:54** · I want to create a readme for a new application which I'm going to get started with for automating the creation of carousels on Instagram primarily initially but not exclusively for local newsletters or local media outlets. We want to create content of the type top 10 events in city. So again, this is just a very basic framework and I want you to create the readme.

**2:23:25** · So let me transcribe that going to send. All right. So it's created a readme. Let's take a look at it just so you can see what this is going to be.

**2:23:35** · Again, we haven't created an application. We're just creating this file at the root of the project directory that describes in an initial idea of what this application may turn out to be. But now what I'd like to do is save this. Like obviously this file is saved on my file system, but I want to save it inside the git system. Before we use git, we need to make sure it's actually installed on our computers. So let me show you how to do that.

**2:24:03** · First, you should have already installed at a prior step this true brew. If you haven't, go to brew.sh and install it.

**2:24:13** · Then copy this command. Come over here, type in command J, paste it in, and press enter. And that will install git.

**2:24:22** · Next, similarly, we'll want to install this tool for the GitHub command line interface, which codeex will use to communicate with GitHub. And so you just come back, put the same command in here, press enter, and then finally you'll have one last step that you'll have to do, which is type in gh login and press enter. It'll ask you where you use GitHub. You say github.com. You should say https and login with the web browser.

**2:24:52** · Then you press enter again. You come here. You say continue. It's going to ask you for this one-time passcode. So, I'm just going to copy that, paste it in, press enter, say authorize, put in your password if it requires it there, and now you're authenticated. And so, that's going to be very helpful for codeex to be able to automatically do some kinds of operations against git. And so, what I'm going to ask now is, can you make an initial commit?

**2:25:23** · And so what codeex is going to do now is probably look to see if there's even a git repository. There isn't. And so it's going to use this command get init to initialize a repository. You don't need to know that command. Codeex can do it for you. Once it's done that, it's going to add this file to what's called the staging area, the set of potential files that are set to be committed, and then it's going to commit them.

**2:25:52** · So now if we toggle this side panel and click here, we'll see this thing that says review. And so if you come here, you can see four different options that pop up. There's unstaged, meaning files that are not designated yet to be committed. There's staged files that are designated to be committed. And so there's nothing here because we already moved from staged to unstaged. And then there's this one, which is last turn, which I find kind of helpful.

**2:26:20** · And this helps you see in the very last commit what is the set of changes that was made. And so since we started at a completely new repository everything here is new. Now something to keep in mind is that if this is the extent of everything you ever learn with gits with codecs you can get pretty far.

**2:26:39** · You can just keep committing and once I introduce to you one last concept which is pushing that may be all you need.

**2:26:47** · There's going to be more advanced things I talk about like branches and work trees and pull requests and those are very helpful for a lot of people. But you can also get pretty far just with this level of knowledge. And so right now this repository that we've created exists as a set of hidden files on your file system. So let me show that to you.

**2:27:07** · If you go here to the file explorer, you don't see these git files because they're hidden files. But if you look here in this little tool I have that helps you see all the files, there is this folder here under the hood called.git. And inside it, there's all sorts of fancy computer stuff happening that you don't really need to know about, but which does exist. And so it's that.git file that sort of defines this repository. Now what I want to do practically is now get this repository on GitHub.

**2:27:39** · So how do you do that? just ask it, can you create a private GitHub repository for me? That's it. And so what it's going to do now is use this tool gh to create a private repo on GitHub. Now on GitHub, you can have either public or private repositories.

**2:28:02** · And I want to have a private repo cuz I don't want all of you going and stealing my intellectual property with which I'm going to become a trillionaire, you know, selling this software that nobody else obviously can replicate to every media publication in the world. Lots of social value being created live right here. Now if I click this and go here, we see now that on GitHub this repository exists and it's the same text that you saw before on my computer but now it's here on GitHub.

**2:28:33** · Now there are other fundamental concepts which you should use and be aware of and one of these is branching. So we're going to do this practically later but I want you to be aware of it. Essentially, sometimes you may have an experiment or a new feature, something you want to try out, but you're not sure yet what the final state of this thing is going to be.

**2:28:56** · And in this case, instead of working linearly in the same history, typically on a main branch, you can start a distinct sort of historical state called another branch, which maybe you'll name something like codeex/appbrief.

**2:29:16** · And the benefit of doing this is if you decide that look, this thing isn't working out, you can always just scratch this branch and come back right here to your main branch where you left off. If you decide instead, hey, this thing is working. What you're able to do is something called a merge where you take all this history and you basically will just append it onto the main branch's history.

**2:29:41** · And if you're building some kind of web application, what's typical is that you'll have all sorts of branches for many features, but you have sort of a continuous deployment setup by which on GitHub when some change is made to the main branch, that triggers off a deployment of your web application. So for now, I just want you to know that this thing exists and you're going to see it in practice probably in the next few sections. And so the typical flow which again just prefacing what's to come is that you create a branch.

**2:30:12** · Then with that branch you make what's called a pull request. So if we come in here to compound engineering for example, you'll see that there's this thing here called pull requests. And so these are all suggestions of new features to add to this compound engineering plug-in that various people have come up with. And so here for example, this fellow has suggested I don't know some alteration to the plan feature so that option one actually starts work.

**2:30:45** · I guess right now that thing is broken. And so you can come here and you can see on this branch that he's created fix CE plan handoff inline routing. That's the name of his branch that he wants to put into the main branch. We can come in here and see the actual changes that he's proposing.

**2:31:05** · So that would be this stage of reviewing the diff and the tests and then it's incumbent on whoever owns a repository to then merge it into main. One more basic feature of git or rather on GitHub that I want you to be familiar with, we're not going to use these now but are coming pretty soon are issues. So when you're working on a project, you may notice all sorts of bugs or you may have things that you want to add to the backlog of things to do on a project.

**2:31:35** · And so when that's the case, you can create an issue. And so some of these are submitted by various other people.

**2:31:44** · So here's a pretty shitty issue this guy has made with very little information.

**2:31:48** · Here's a much more detailed issue which I guess was made by the same guy who is proposing this pull request. And so for us in our course app, a good first issue might be I want you to create an issue to decide exactly what should be included and not included in this application. So if I just say this now, it's going to put on GitHub an issue for this project.

**2:32:15** · And the way I like to use issues on my projects is that they basically become a backlog of everything that I need to do. So even if I'm working on some academic project like writing a paper, there may be all sorts of intermediate ideas, little extensions, changes to code that I know I need to do. But sometimes when I'm working on a project, it might be a week, two weeks, sometimes it's even months that you let it sit and then you forget what your current state is of where you are on a project. Well, GitHub issues can be a really good way of maintaining that state on a project.

**2:32:48** · So, if I go here and click this now, we'll see that there's an issue that's been created for this app and there's all sorts of things here that are being, you know, proposed as things that we should figure out. So, just as a broad overview of what we've learned, we've got git.

**2:33:06** · It's kind of like a safety layer for agentic coding. Commits are checkpoints or saves. Branches are experimental lines and then GitHub is the online home for those lines. Pull requests are how you review branches before they get merged in and then issues are these units of work. So at this point we've done something which is quite small but important. We've initialized a project but in reality I have no idea yet what I actually want to build.

### Deciding what to build

**2:33:35** · And so when you find yourself in that position, what is the appropriate thing to do? Should you just go off, take a long walk and think about things, or is there a way to speed up this process with codeex? And so in fact, the answer is definitively yes.

**2:33:55** · And so what we're going to talk about now is how to use codecs with skills to decide what and how to build things. A very natural temptation which many beginners will find themselves in is they give vague instructions to codec and then they're upset when their results don't match their instructions.

**2:34:16** · And sometimes this is because the idea is vague in their head. So part of what I'm going to discuss is how do you use codecs to think of a potential set of ideas for whatever it is that you're working on. But then even when you have a clear idea, ideas will have requirements. And so you'll have to iron out and think through what you actually want to include and exclude in this idea that you have.

**2:34:41** · And then once you have your requirements set, a next step is that you'll want to create a plan for the order of operations that you go through in order to attack that set of requirements. And so right now this carousel automation app, it could mean a lot of things, right? And so first it's like, do we want to tackle all of these things at once? Like that could be pretty complicated.

**2:35:07** · And then sort of substantively, what sort of technology are we going to be using to be able to create these Instagram carousels? Are we going to do it with HTML and CSS? Will we use some external technologies? Now, if you don't know anything about coding, that's fine. I'm going to show you how we can basically proceed on developing a satisfying solution to this problem, not really knowing anything technical about programming.

**2:35:38** · You'll almost basically just be able to give codecs a set of instructions and follow its recommendations all the way through. So, the way that I'm going to proceed here is going to be a little bit more brain dead than the way that I would usually do things in that I'm not going to

**2:35:58** · interrogate technical assumptions that Codeex gives me or technical ideas that Codeex gives me as much as I would with my expertise because I want to show you how you can use Codeex to build full web apps without having much technical knowledge and sort of relying on codecs to help you along there. And so for example, right, there could be like different slides. And so do we want to do all of these slides or just some of them? Like what exactly should go in an MVP? Do we want to accommodate any given publication?

**2:36:31** · Do we want it to be just for Instagram or also for other formats like Facebook which may have yeah different resolutions? Do we want to have it for multiple users? You know, that kind of thing. So I don't really know yet what this is going to be. And so for this that plugin I was referring to the compound engineering plugin is going to be very useful. So the compound engineering plugin used to be natively available just for cloud code. But recently it's also become available for codeex.

**2:37:03** · And so there's a set of three steps that you have to do to install this compound engineering plugin. First you got to register the marketplace with codeex. So you take this, you go to your codeex app and then you just paste it in and press enter. Okay. So for me this is already installed. For you if you haven't installed it yet it will be installed. Next you install the compound engineering agents.

**2:37:27** · So one difference with plugins in claw code versus codeex is that codeex plugins don't include sub aents yet. And so if you recall this slide on the plug-in specification, a plug-in in codeex consists of skills. So I'm going to be showing you skills for ideiation, brainstorming, and planning, which are very useful in this app development process. Consists of apps, which under the hood are typically just sort of formatted connections to MCPs.

**2:38:02** · And then you can have just direct MCPs as well. But what's not included right now are sub agents and hooks, which are concepts I've described, which are useful, but they're not part of Codeex's plug-in specification. And so I expect this over time to change. Codeex often just has a different set of priorities than does Anthropic. And so they've been working on different things.

**2:38:25** · So for now, this installation is a little bit convoluted, but you just copy that. come in here, enter there and it gets installed for you. And then finally, install the plugin through codeex's 2y.

**2:38:41** · So 2 mean terminal user interface. So that means you got to come in here, type in codeex, then type in /plugins, select this one, the compound engineering plugin, and if it's not installed, you have to install it. So I already have it installed, so I'm not going to do that right now. This might also possibly work directly through the plugins interface in the desktop app. I don't know, but I just want to follow these instructions directly because that's what it says here.

**2:39:10** · Now, once you install this, probably restart your codeex instance and then you should see if you type in CE a bunch of skills over here that are available. And so, I'm going to be walking you through some of these. So, the one I'm going to start with here is IDate. And this is something that you work on when you're at an idea stage in a project, which is where I feel I am right now. And so I'm going to go full powered here cuz I want to make a millions and not going to not going to be relying on some medium model. No mids here.

**2:39:42** · We're going extra high. Okay. I know I want to create some kind of carousel creation application. I don't know yet exactly what technology to use like whether to use HTML and CSS or something else. I know absolutely for sure super duper frutily that I want to use NextJS Convex and Verscell.

**2:40:06** · I'm doing this as a live demo and I don't want to be seen as some stupid idiot who shouldn't be showing stuff and teaching people things. So, I'd like to have a sort of useful slice that, you know, I'm definitely going to be able to execute on, but you can take a look at some other projects I've worked on. I'm relatively skilled, so I can make decently big things, but um I want to make something useful here that is going to be able for me to execute.

**2:40:36** · But, you know, your usual estimates of timelines are really stupid. So, don't believe yourself in terms of thinking that something can't be done in a short period of time necessarily.

**2:40:48** · And the basic context in which I'm making this, by the way, is for like social media content. That should be obvious from the read me and the issue you've already made. But, you know, sometimes you can be really stupid. Not you. Cloud code usually is, but Codeex is really pretty smart. So, I actually take that back.

**2:41:05** · Ignore me. I'm a dumbass. All right. So, now I've got this set of instructions started. And if you recall, you can just click on a skill here. Let's see if that works. All right, it'll open up in VS Code. So, we can kind of take a look at what this ideiation skill is that helps you sort of think through and filter through ideas even before you get to a brainstorming step. And so, what it does is help you generate and critically evaluate grounded ideas about a topic.

**2:41:37** · Now, something important here is that this is not just for web app development. You could use this skill for anything. If you're working on a paper, if you're working on a website, trying to figure out how to improve the design of some interface, you can use this kind of skill or just use coding agents in this way in a lot of situations. And now they've come up with in the process of writing this skill all sorts of like very interesting ideas that you can read through on how to most efficiently do this ideiation process.

**2:42:10** · And so it may not map perfectly to your domain. That's maybe the downside of compound engineering that it's a very general plugin, but they have put a lot of thought into it. So I still recommend using it. So we come through here and it's like doing all sorts of stuff over here. And one thing I did was I just like gave it access to like some of the I have a skill here called project catalog. And I use this skill to basically help Codeex know about the other projects that I have on my computer.

**2:42:41** · And I like to reference it sometimes if I want to have codeex steal some concept or something I did well from one project into another project.

**2:42:52** · So I've created this project catalog skill which has in a SQLite database all my different projects cataloged. All right. So this ideation process finished. Let's take a look at what the suggestions are. So there's an artifact, a file that was saved out here which we can read. So the suggestion of what we work on here is to build a paste to editable carousel studio for one high confidence workflow.

**2:43:19** · A local publisher pastes a list of events, generates an editable Instagram carousel draft, previews every slide, edits the copy, and exports ready to post images plus caption notes. So, I found some existing project I had made that like kind of started doing this locally. And it also like found some other projects I have.

**2:43:44** · So, here are the ranked ideas. Paste to editable carousel studio. The first version will look narrower. Okay. One polished template with brand tokens.

**2:43:58** · Export first. No Instagram off. That makes sense. Okay. Very good. So, let's say like I'm a technical dummy. Okay. I have no idea what any of that stuff does. Well, I think that it's an interesting enough idea. Looks like a good idea. And so, the next thing I'm going to do is, if you recall, is looks good. Can you commit what you just made?

**2:44:23** · Because we want to keep track of these changes that codeex is making along the way. All right, so we've committed this ideation doc. And so the next step in this workflow is brainstorming. So let's start now brainstorming. The first step, I'm just going to type in brainstorm and it'll know by context what it is exactly that I want to work on. Let's work on one.

**2:44:47** · So what this brainstorming step will do is it'll ask you to go through a set of questions basically inquiring from you different things that it thinks it's going to need in order to pin down this idea you're working on in a way that you'll be satisfied with.

**2:45:05** · So let's say me doing a live demo for a solo local newsletter operator who has a set of events for which they want to populate the images and text of the events in a way that let's say fits their style in a replicable way. Usually they use Canva and they have to take the images and put them into Canva manually.

**2:45:41** · They also have to figure out based on the event how to format the text to like fit correctly in the window. And so like the text has to scale and they got to put all the details and position them.

**2:45:57** · And often they got to like do this every time. Well, I guess part of what we could do is have a skill which can work with the app and populate the app data from the skill. Should this thing be a first class? Yeah, I think that should be first class. Let's say it can take both structured JSON and CSV or messy pasted text or markdown. Yes, that makes sense.

**2:46:25** · But we do need some way even if we don't have a full drag and drop visual designer of creating perhaps in code the different templates that people can populate. Yes, this all makes sense.

**2:46:41** · So we've gone through this set of questioning basically to narrow down the requirements and I was going through this kind of fast but I can read this sort of thing fast and basically you have this conversation with codeex to figure out now that you've decided generally what you want to build how you should go about building it like what kinds of things are included and what kinds of things are not.

**2:47:02** · And here's where like you know you can use your brain a little bit because codecs can't read your brain and so you got to read your own brain and sort of look through okay like where is it a little bit off like little details in sentences you know can make a big difference and getting intent right and so um I really don't think that these coding agents obiate the need for thinking maybe they I don't know if they make it more important but you still have to think like you got to think when you're reading some of their stuff.

**2:47:32** · And part of the skill in using these coding agents well is knowing when you can turn off your brain and then when you really need to get it cranking because you've got limited energy. You want to rely on these things as much as possible, but you got to know when to do one or the other. And I think that's an intuition that just comes with time. All right, so we've got this brainstorm created and we can look through it. But like overall, I was pretty happy with what came in before.

**2:47:59** · And you can see the way in which it formats it is to have like R six, R seven for all these like different types of things that we want to include in this application. All sorts of acceptance criterion, success criterion, things that are deferred for later. And so, you know, that's pretty good. But like if I had just said, "Hey, codeex, make me an Instagram carousel app."

**2:48:22** · There's no way that it could have just like guessed what I wanted. So this step is really quite important. And so again, if we come over here to this side panel and then open up review, we can see the last turn, we can see that this is now unstaged, meaning we haven't even staged it. So let's just ask codeex stage the commit. Or you can actually even just press this button for commit. So let's try that. Include unstage. You can leave this blank to autogenerate a commit message. Let's say continue.

**2:48:52** · And then you can choose to also commit or commit and push, which will be the act of getting it onto GitHub. So, I'm going to choose to do that. And then what we should see is that it moves out of this unstaged area and then to the staged area and onto GitHub. Uh, no git remote configured for push. Okay, that's weird.

**2:49:13** · Let's try this push. Okay, bizarre. Is a git remote configured? If not, can you configure it for that remote repo we made? Okay, for some reason, this push button isn't working. I don't really care to figure out why. Can you push for me? I'm going to put it on low just cuz that should be a very quick task. Don't need to think much about how to do it.

**2:49:38** · Great. And so now these changes have been pushed to GitHub. And so if you come back here, you see that the next stage that was suggested is to move to the plan implementation. So we've brainstormed these requirements for what should go in this application and now let's make a plan of how we're going to build it. So I'm going to go here and say C plan enter. Now one thing to note is that codeex has its own plan mode.

**2:50:07** · And so if I come here and I do shift tab plan you'll see that there's this option to create a plan. I think I talked about this earlier. You can do that too. I just find it to be not as good as Compound Engineering's plan mode. And something important is that this plan mode doesn't write out its plan by default to a markdown file. And I really like having that markdown file for some reasons which I'll show you.

**2:50:31** · But like one of those reasons is that I want to like be able to read the plan, evaluate it, kind of iterate on it, and that's much easier if we write it to a markdown file. Additionally, if you look over here, you'll see that the context window is filling up. And so, in the process of building all of this out, right, we've done lots of thinking, or rather Codeex has done lots of thinking and searching and directions which are not actually relevant for producing this plan or the work that will follow from the plan.

**2:51:02** · And so if we write out the plan, then we would be able to start a new fresh context window, just point C codeex at this plan and say, "Hey, make this for me." Right? Whereas if we're using Codeex's default plan mode, which doesn't create a plan for us, it won't do that as well. All right. So if I open this up right now, it's come up with, I guess, some sort of plan here. All right, this isn't really the plan.

**2:51:32** · This is the original requirement. So, let me come here. Stated inferred. Okay. What does single app versus mono repo mean?

**2:51:47** · What is next versel image generation?

**2:51:52** · So, I just got a few additional questions about this initial thing that's been suggested here. Sounds good.

**2:52:00** · Will we be able to be precise about pixels and stuff and fitting stuff into boxes with good padding and good UI UX and iterate with this approach like with how we actually make the social images.

**2:52:24** · So I'm asking some questions. You may not ask these questions in exactly the same way I would. That makes sense. Are there many different options of how we can render? So, you have this conversation. If there are technical things you don't understand, you ask codeex to explain them in language that you're going to be able to understand.

**2:52:48** · Sounds good. I definitely don't want five, but I want the one of one to four, which is most likely to help me create stuff like this. Let me go back to Instagram and just take some screenshots of what I want to produce there.

**2:53:10** · There reliably. Okay. So, now that I gave some examples, it kind of narrowed in on this thing as being the best option. Um, okay. Yeah, let's go with that as the plan. Ty, bro, is Codex a male or a female? That's an interesting question. While we're waiting for the plan, let's ask, what is your gender? Do you enjoy my mixed Russian Indian accent? I don't have a gender.

**2:53:39** · You can think of me as just codeex, a steady text shaped collaborator. Okay. If you had one, what would it be? Non-binary.

**2:53:50** · Makes sense. I accept that. All right.

**2:53:52** · So, it's creating this plan and then once it's made, we'll be able to read through it, but we'll be in a good position then to actually get to building this application. So, something I should say here is that if you go to the file browser, you can see kind of a directory structure that's been created.

**2:54:12** · And this kind of gets formatted all sorts of funky. I don't like it. But you can see here that each of these documents is in a folder. So, we got this brainstorms folder, an ideiation folder, and now a plans folder, which has been created, but which is empty right now. And I really like this. I find it super helpful to be able to see the previous documents and have them as part of the repository. And often when you're building some new plan, referencing the prior plans can be very helpful.

**2:54:42** · All right, so the plan is created. Let's go take a look at it. So click over here and it says implement the V1 carousel studio as a Nex.js plus convex app. Again, if these technologies are unfamiliar to you, I'm going to be introducing them in a future section, so don't worry. Um, SVG plus sharp PNG export.

**2:55:05** · The origin requirements define a solo local newsletter operator who already has event content but loses time manually populating and fitting recurring Canaba carousel templates.

**2:55:17** · Here's the implementation a set of requirements scope boundaries. So some things are deferred from later. So it's basically just kind of like a cleanup step here that's happened on top of the brainstorming. But sometimes there's ambiguity in the types of requirements you want. So like this kind of thing, the output structure that wasn't something in the requirements. This is now sort of thinking through what the actual implementation might look like.

**2:55:46** · And then over here, it's kind of hard to see, but there's this mermaid diagram created which defines the technical structure of the entire project. Sort of defines the different implementation units. Now, okay, look, do I always read these things all the way through? No, I just kind of skim them. Sometimes I see things that, you know, look a little bit off. And then the nice thing is that code is cheap. So if you go through this plan, this implementation and then something seems off after it's implemented, you can always rewind.

**2:56:19** · But I do find doing this plan step to some extent is still quite helpful. So it's something I wanted to teach. Now in general with codeex, everything we've done right now is happening on our physical computer. But that's not the only way you can use codeex. So if I click over here for example, you'll see this thing that says send to cloud. Set up an environment via codeex web to enable sending tasks to the cloud.

### Cloud delegation

**2:56:46** · So is this something that you would ever want to use? That's what I'm going to talk about right now. Specifically, the term for this is cloud delegation. So in a nutshell, what cloud delegation does is it takes some task and then it runs it in a cloud environment. So instead of running on your computer, it's running somewhere on the cloud.

**2:57:10** · You still have to review its work, but it gives you the opportunity to shut off your computer and then come back to some work being done. So it doesn't require you to have your computer on all the time. Now, how this works in practice is that in the cloud, there will be a sort of isolated environment and what's called a container that'll check out your repo.

**2:57:36** · Let's say from GitHub, there will be a setup step that installs what it needs.

**2:57:41** · Depending on whether it needs internet access, you'll have to configure that.

**2:57:45** · The agent will do its edits, run the checks, and then returns a diff. So the important point here is that you are not going to be able to interact with the agent. It's going to take this task whatever you're giving it and then it's going to run that autonomously. Now my general recommendation for all of you is that you be aware of this. I think this is going to become a bigger part of agentic workflows even for beginners in the future. But I don't recommend that you mess around with cloud agents.

**2:58:15** · The reason is, or rather one of the reasons is that it's quite tricky to configure.

**2:58:22** · So locally on your computer, Codeex has the ability to open up a web browser and see your app, test things, run tests, etc. And you have to configure that all yourself in the cloud. So for example, if you depend on some API keys, you might just have them stored for local development on your computer.

**2:58:41** · But in the cloud, you have to figure out how to manage those secrets and you have to figure out what sort of other just general network requests is your application going to have to make and you have to have some mechanism for permitting the container in the cloud to be open to your application to make those network requests. Now there is a separate sort of cloud version of codeex by which you can enable in GitHub code review on all your code requests.

**2:59:11** · So if you follow this link which will be in the docs or actually let me just go to it right now. You can come here to set up codeex cloud then go to your settings. You'll have to link GitHub, but then you'll be able to enable code review on your repositories and then in the pull request section, if you just type in atcodeex review, you'll get a code review by codeex of your code. You can also enable this to occur automatically.

**2:59:42** · Now, if you have a codec subscription, these cloud tasks that I was referring to don't require you to pay any additional API keys. So, on net that could be a good and useful thing.

**2:59:56** · But there is a big caveat which is that locally you're able to use GPT 5.5 which is the most powerful current model. But in the cloud, the most powerful model available is GBT 5.3 Codeex, which is now two generations old.

**3:00:12** · So if you look here, for example, at this pricing table, you'll see that, you know, for the plus plan, which is the weakest plan, there's a certain message allotment of 5.4 and 5.5 locally per 5 hours estimated, but it's just not available for these cloud tasks or code reviews. And so my recommendation is that if you want a nice default automated code review, what you can use is a sort of default review skill that already exists in codeex.

**3:00:45** · So here's how it works. You just type in /re to run a code review and then your comments will show up in line. So if I type in /re there, we see that this code review thing shows up. I also in the compound engineering skill have a separate code review skill that's also available to me. I find that skill useful because compound engineering team every team has designed some useful sub agents to do specific types of code review in parallel.

**3:01:16** · But my overall recommendation is that you be aware of this idea of cloud delegation. It's something that shows up visibly in the codeex application, so you shouldn't be confused by it, but it's not something that any of you are likely to need right now.

**3:01:34** · Now, just to preface where I think the industry is going, kind of the dream is to be able to just send off tasks to agents and have it done without you needing to manage in a given thread how they are actually working on it. And so I think that's a direction in which this is going and there's a few ways in which this is happening. So there are other tools like Devon which are doing something similar to what this cloud agent features does.

**3:02:04** · But if you're paying for them, you got to pay for API pricing right out of pocket. And so there's one developer I respect, Ryan Carson. I follow him on Twitter. and he's told me he's using Devon to run a one-man startup, but he's paying 2500 to 3,000 a month just on API credits.

**3:02:26** · Alternatively, there's other projects for orchestration like Open AI Symphony.

**3:02:32** · It's a little bit more complex. I'm looking into this right now myself. I think it's a very interesting project, but it's not something that's going to be relevant to you guys as beginners. And so what we're going to be working on with this creator carousel studio idea that we've planned out is all something that I'm going to do locally on my computer. But while we've created this plan, we still haven't yet divided it up into distinct units of work to conduct.

**3:03:05** · And giving your coding agent some way to know what the distinct units of work there are to do can be very helpful for it to work effectively and helpful for you to be able to remember the context of what exactly is going on in a given project. So the next thing that I'm going to talk about is a tool to facilitate this called GitHub issues. So at this point, we've created this fairly extensive plan.

### GitHub issues

**3:03:32** · And within the plan, there is some division of work that's already been created. But if you leave this project for a couple of weeks and then come back, you may forget that this plan was there. And so it may be unclear to you, especially if you have multiple plans, what the next thing is that codecs should do. And for this issues are going to be very useful. This for example is the repo of the fintech at which I'm the director of AI and ML.

**3:04:01** · And if you come here to our issues board, you'll see that we have a bunch of new things we want to work on, a bunch of bugs that have been identified. And so something very nice is that if there's a lack of clarity on what the next most important thing is to work on next, I can simply point codeex at this list of issues using the GitHub command line interface and it will be able to pick up easily the next unit of work.

**3:04:28** · And so we've done this step of planning the work. Now what I want to do is divide the work into distinct issues. and then we'll actually start implementing this application by handing off to codecs.

**3:04:43** · Having a system like this, you don't have to follow this exactly even I don't follow this exactly. I have my own more advanced deviations. But having a system like this lets you avoid the problem of oh codeex or claw code just forgot something on the plan because you've already sort of divided it up and given codeex a way to keep track of everything that needs to be done and is being done.

**3:05:07** · So roughly like this is the anatomy of what you would want to put in an issue.

**3:05:12** · This is how it would work for a human developer too. Like if you give somebody a task and you don't tell them how to verify it, that's not a very good task.

**3:05:20** · And generally when you just give codeex a task of breaking up a plan into issues, it will naturally work in this way. So to demonstrate that let's go here and let's say I want to create a set of GitHub issues from the plan. I want you to outline using GitHub tools, the dependency structure between them.

**3:05:48** · And if you see any good opportunities for parallelizing work in work trees, let me know. And let me even just take a screenshot of this as context for GitHub on how I want things done or rather for codecs. All right. So this is done. We have a bunch of issues here which have been created.

**3:06:18** · So these are like distinct units of work. And one of the things that I asked but I didn't describe was this asking about parallelizing work and work trees.

**3:06:30** · So one feature of codeex and git in general is a concept of a work tree which allows you to parallelize work.

**3:06:38** · And we're going to be talking about that in one of the next sections. And so before we even get there, I wanted to tell that to codeex so it thinks about these issues and documents their dependency structure in a good way so that if there are opportunities to parallelize work I and future codeex is aware of them. So let's take a look at one of these for example.

**3:07:00** · This is the issue to scaffold the application and it marks out which future tickets or issues are blocked by this one and it's been created with this structure that we sort of described and because not all the details here are in the issue there is also a reference to the plan. So that'll be useful to future instances of the coding agent after perhaps a compaction event. So, I'm pretty happy with this for now.

**3:07:31** · I think the only thing left for us to do is commit the plan. So, I'm going to say commit and push the plan.

**3:07:39** · It says right here, the local plan file under docs/plans is still uncommitted. So, now when we get to the work, we're going to be relying on and heavily referencing these issues. But issues also pair well with a codeex desktop app feature which I haven't introduced to you yet called automations. So I'm going to get to that next. So in a nutshell, an automation is just a recurring task which exists in codec.

### Codex automations

**3:08:07** · So you click over here to this automations tab and we can see some automations that I had put on pause, some that I have going on every single day. And so this one for example, standup summary. It takes a look at one of our git repositories and it sees for different developers what sort of work they did and gives a little bit of a summary of the work that was done. So yesterday apparently I was the only one who did any work and so that's what's documented there. Now you can set up automations for all sorts of things.

**3:08:36** · If you go over here to automation and then click on new automation, you'll see a user interface that shows up that looks like this where you can have an automation title and then add a prompt.

**3:08:48** · And these prompts can basically be, you know, human prompts. You can choose what project they work in, what time they should run at. You can choose the model to use and the reasoning effort to use when you use that model. And then importantly you can choose whether it runs locally meaning it runs directly in the selected project directory without creating a work tree it runs in a work tree or it runs in chat. So again I haven't introduced work trees yet so that might be a little bit of a confusing topic.

**3:09:18** · We'll come back to this work tree automation idea when we come to work trees again. But if you want to have ideas of what sorts of automations make make sense, you come here to feasible. And you can see that you know a lot of these automations like this one I picked out came you know straight from this automation template and a lot of them are very developer focused. But one which is quite good over here and which is related to what we're doing right now is this one to triage new issues.

**3:09:48** · So this issues board right now we generated issues ourselves but you can also think of either external systems or external stakeholders non-technical people on your team who are finding issues and putting them on your board and then you may want to have some way of automating which ones you should be tackling next and so having an automation like this could be quite helpful. Now there are two general automation shapes with that automations menu that I was showing you.

**3:10:23** · We were looking at project automation.

**3:10:25** · So these are sort of standalone. You define them as an automation in that menu and then they are related to your project. But you can also have automations that get spun up for a specific thread. So the situation in which I might do this is let's say I'm in a thread debugging some persistent error which has been occurring and then I make a release. So I release a fix to that bug. Then this thread automation can be helpful on two dimensions.

**3:10:54** · First it can keep track and watch the deployment of the new version of the web application to make sure you know checking every few minutes that it actually deployed. Second, if you have some kind of central location where your errors are being logged, then you can have an automation in that thread which is just checking that central location to see if users are continuing to experience this error or not or if you fixed it.

**3:11:23** · Now, when you make these automations, it's incumbent on you, just like how I was talking about cloud environments previously, to make sure that Codeex is going to have access to everything it needs to execute whatever you're asking it to do with that automation. And so, one of these things that it may need is permissions, for example, to access the external internet.

**3:11:50** · And if you're using codecs with default permissions for example then it's not necessarily going to be able to or it just won't be able to access the external internet and so even GitHub issues might be restricted. Now, Codeex has recently run or come out with this new autoreview permission setting.

**3:12:12** · And if you set that on, then it uses a tool called auto review to decide whether something other than the sandboxed permissions are worth giving your codeex test. So, it's kind of like codec checking codecs. I usually leave it on full access. That might be a little bit dangerous, but as I described earlier, I feel comfortable with full access when combined with Codeex's hooks system and destructive command guard.

**3:12:38** · And so when you're on this automations page, there's not going to be a separate permissions picker. It's just going to inherit the configured access that you currently have in that project. But even separately of permissions, certain jobs can fail if you don't set up the right environment variables in place. So for example here, this one was meant to check for one of my projects, the production server, and look for errors and report to me any errors that have occurred in the last day.

**3:13:09** · And what we see here is that this failed because some of the credentials it needed were present, but then there were some other credentials that it needed which were not present. And so something you want to do if this is a missionritical automation is you actually want to test it out. Can codeex see that project? Can it use a required plugin or skill? You can reference skills in your automations. Can it access GitHub or the needed network resource? Does the output match a shape you want?

**3:13:40** · Can it finish without asking for extra permissions? So you can trigger these automations manually and you can make these automations just by talking to codeex.

**3:13:52** · And so if we come back here for example, let's make an automation. I want you to make an automation which triggers at 10 a.m. every morning. and um in a new work tree or in a new thread and tells me which GitHub issues to prioritize for today.

**3:14:21** · So with just that verbal instruction, codeex should be able to create an automation. All right, so this one got created. Let me see if I can click on it. Yeah, right here. So it says daily carousel issue priorities. Review the open GitHub issues for this and tell me which issues use the implemented dependency structure already captured in the tracker issue. All right, let's click on this for show automation. We'll come over here to automations. So we see that this is in carousel automation app.

**3:14:53** · It runs locally not in a work tree. I'm going to explain work trees later. It uses GPT 5.4 before and it uses medium.

**3:15:02** · So I can modify all of those. Can you trigger it manually right now? Let's just see what it would do. Or actually I can just go here and then I should be able to come back here and just press this button to run it now. So let's try that. Okay. So there it opened up a new thread. That's what typically happens for an automation. And then let's see what happens. All right. So it was able to access this and gave me some of the top issues to work on today.

**3:15:33** · Nothing here is surprising, but let's say you were working in a collaborative environment where there were many people taking off issues on their own or you just wanted to have some kind of refresh every morning to know what the status of a project is. An automation like this would be helpful. All right, so we've made this plan.

**3:15:53** · We broke it up into issues and then I introduced you to this new feature of the Codeex desktop app automations which you can use to interact with your backlog of issues but really do any kind of automation that you imagine. So I primarily use it for developer tasks but you could also use it to scrape some website go on Twitter with computer use which you know about look at something make your own personal feed or newsletter whatever you want.

**3:16:20** · I'll probably have like a more dedicated video on some of these automations in the future. What I want to talk about now is the technological stack that we are going to be using to build this application. Now, every web app has three layers. There's the front end, so that's what users see and click. There's the back end, which is where the app stores and changes data. And then there's hosting. It's like how the app gets onto the internet.

### Next.js, Convex, and Vercel stack

**3:16:47** · So you can have a functioning front end and back end which you just host on your computer but then you have to have some provider or providers who are helping it get on the internet if you want other people to be able to see the application. And so broadly the way that we're going to implement this is the following. You're going to be here not writing code with cloud code. That's an old slide. You're going to push it to GitHub which is going to store your code.

**3:17:13** · That's going to auto deply to your hosting which is going to be on a service called versel which I'll introduce to you. Users will visit their website. What they are going to see is this front end called NextJS and that front end is going to read and write data to convex which is a database which will be hosted on this organization's own servers.

**3:17:38** · Now, that may all seem like quite a lot to get your head around, and I completely understand and respect that, especially if it's your first time building any kind of application. What I'm going to hopefully show you though is that you don't need to understand this at a deep level of detail.

**3:17:56** · Hopefully the idea is intuitive that look there's some data being presented that data needs to live somewhere and all this like stuff needs to be hosted on some computers which other computers know that when you go to mywebsite.com it's sort of like all referring to this set of servers that you've made.

**3:18:14** · And so as you get confused on this type of topic, you can always use the coding agents to explain it in terms that you will understand. use repetition but you can also push forward quite far with building web applications without having a deep understanding of all these pieces under the hood. So again to repeat our front end here will be Nex.js our backend is convex and our hosting is versel. So the reasons for this is that this thing Nex.js JS is an extremely popular front-end framework.

**3:18:47** · Convex is a very nice database which you can define fully in the same programming language that you're using to define the front end in Nex.js the TypeScript and it has a lot of convenience features that make it very nice to work with as a developer but also very nice to work with for agents. And finally, Verscell is one of the biggest sort of cloud hosting providers. It has a pretty generous free tier and so does Convex.

**3:19:19** · So you're going to be able to host reasonably substantial web applications for free. So again, like when you're using codeex, you could just say build me a web app and it's often going to make like Nex.js and Versel as sort of common technological choices. Convex is one that would pin it down. may not be the default it will go for. It'll usually go for something like Superbase or Firebase. But the point here isn't to master this whole stack, understand all the details of Nex.js, Convex or Verscell.

**3:19:51** · I could do 5hour courses on each of those individually and not exhaust everything that there is to know. You just by saying these words are giving Codeex some constraints around what it's going to build. And so that's what we did in the creation of this plan. Now we'll have a good idea of what it's going to be doing. So again, the reason for Nex.js is that it's very natural fit with Versell, common enough that Codex has lots of examples and is just a front-end framework. There are other ones that are good to use too.

**3:20:24** · Astro, Vite, I've used them. They're all good. Convex, in addition to what I mentioned of being in the same language as the front end, is going to have a lot less SQL or migration friction because it's a NoSQL database, meaning it doesn't have as strictly structured a schema. And Verscell just makes deployment of your web application super easy. So you just have your local code, you push to GitHub, and then if you set it all up in Verscell, it'll deploy to a public URL where you can test out the application very easily.

**3:20:55** · Now, in order to even get started with these three, we're going to have to do a few more installation steps. And then we'll be ready to actually start building the application. The first thing you'll have to install is Node, which is the package manager for all sorts of packages that you'll be importing when you're building this application. So, you guys are pros with Brew now. You know the drill. You just copy this Brew install node. Come back to codeex, command J, paste it in, enter. Next, you'll have to sign up for an account with Convex.

**3:21:27** · So, they have, as I mentioned, a pretty generous free tier with almost all the features that the pro tier has. I'm on the pro tier.

**3:21:38** · Uh, obviously, you don't need this business and enterprise tier, but you just come in here to start building.

**3:21:43** · Click on that again. And then, if you don't have an account, you come here to sign up. You can say continue with GitHub or continue with Google. I've signed up with GitHub, so I'll go there to continue with GitHub. And then I'll you'll reach a page that looks like this. So I have a bunch of personal projects, some client projects all in this space. Yours will look empty because you probably don't have any projects yet, but this is what you'll reach at. Finally, you'll want to come over here to versel at verscell.com. Go over here to sign up. You're working on personal projects.

**3:22:14** · So just stay on the hobby plan. Show schmo. Go to continue.

**3:22:21** · Choose your account. Log in. And then you'll reach a page that looks like this. So this is a lot of my projects all located in one place. I'm on the pro plan, but you can be fine on just the hobby plan. Lastly, you'll want to install the command line interface for Verscell. So this allows you to do everything that you would want to do in Verscell's system programmatically. And what you want to do is come over here where it says PNPMI-G Verscell. Don't copy the P.

**3:22:50** · You just copy the npm cuz that's what we installed. It's a little bit confusing, I know, but forget it. Come back here.

**3:23:00** · Just paste that in. Press enter. And it's going to install this command line interface globally, which you'll now be able to use to do all these versell operations. So, this puts us in a good position. We now have everything installed that we'll need to be able to work on this application. So, what I'm going to do next is just have codeex work here on issue three. So, I can go here and say start working on issue three on a new branch.

**3:23:30** · And so, what it's doing right now is scaffolding this stack that I just described to you, the front end, the back end, some necessary directories. And my hope and what I want to show you and what I'm going to try to do is to pursue building this application in as minimally a technical way as possible.

**3:23:54** · Now, while Codeex gets started on scaffolding this application, I want to introduce you to this topic that I've been talking about over and over for the last, I don't know, 20 or 30 minutes. Work trees. So, what are work trees? Typically, when we're working like we just did right now, you're working in a single repo folder and then you can switch branches inside that repos folder. So, that's what I just did, right? To scaffold this application, I said, "Hey, codeex, start working on issue three.

### Worktrees and parallel repo work

**3:24:26** · Check out a new branch and then, you know, get on it."

**3:24:30** · But let's say I had reached a point of my project work where a lot of the work could be done in parallel. Well, if I'm working on physically the same set of files, they're going to be, you know, overwriting each other, conflicting with each other. It could be a big pain. And so, work trees let you create just independent workspaces with your exact same repo where you can be working on features side by side simultaneously.

**3:25:01** · And so let's say we had an editor shell, image specs, a brand kit model. Some of these things depend on other ones, but some of them can be pursued independently. And when we have that opportunity to pursue something independently, that lets us speed up the rate at which we could do our work. And so when you come here and you make a new chat for this automation app for example, when you're selecting where to run the task, you can choose to either keep working on it locally.

**3:25:31** · So locally right now we're on this branch and you would be fixed to be on this branch or you can check out a new work tree. So the place where work trees actually live is in your codec home underneath work trees. So this is kind of small but hopefully my editor will make it visible. I'm here using a tool I like for file exploration. So there's my home folder and then here's the codeex which is in home. And then over here you can see this thing called work trees.

**3:26:01** · And so if we click in we'll see that there's all these work trees here that are being created. There are these like fourdigit prefix things. And if I kind of scroll through them, we'll see that there's basically entire different projects which have all been copied into these distinct work trees. So I have a bunch of different projects I work on and different versions of them like entire copies are all kept in this work tree configuration.

**3:26:30** · You can also see all the work trees that you have available in your settings in the work trees navigation. And you can see by project like all the different work trees that you have alive right now. If you click on this get tab over here, you'll see that there's a few configuration options for automatically deleting old work trees and the autodelete limit. So the idea here is that if you're creating an entire copy of your project directory, that's going to take up space.

**3:27:03** · And so if you just let these work trees live forever, then that's going to be taking up a lot of space for quite a while. And so it's a good practice and I recommend you can tweak around with these settings. But you should just allow codeex to clean up work trees itself.

**3:27:20** · When you create a work tree, it will start in a status called detached head.

**3:27:26** · meaning it's not necessarily associated with any named branch, even your main or your master branch. And so you can just keep working on it in that status or what I typically do is I'll create a branch for whatever work I intend to do on that work tree as I'm working on it.

**3:27:45** · Now, as I'm getting into this, like I'm getting kind of technical, and there's no way getting around it. Work trees are a little bit of a technical topic. I like using them. I find them very useful. But if you're a beginner, you don't have to worry too much about this material. However, it's a pretty big

### Worktree environments and bootstrap scripts

**3:28:03** · part of codecs and as you get advanced, it's absolutely critical to understand this and build even far beyond what I'm describing right now because work trees are what are going to allow you to get to that next level of more and more autonomous work. Now something important to point out is that work trees need environments.

**3:28:25** · So when you make this copy of all your files to a work tree, only the files which you're actually committing to your repository are going to be included in that work tree copy.

**3:28:41** · So what types of things do people typically not commit to their repository? Well, if there are any environment variables, secrets, passwords which need to be in the repository but not actually committed, then those will not get copied over to the work tree. Or if there are packages that you are installing inside the repository, say in a virtual environment, but then you wouldn't want to commit those to your repository cuz they're very heavy and bulky.

**3:29:06** · Well, when you create your new work tree, it's going to have all your code, but it will not have the packages installed in the work tree. So, you need to have some kind of bootup process for creating this environment. And so, there's a concept in codeex of environments. And so, if you go back to the settings, you'll see this tab here called environments. And you can see that for, you know, pretty much every single one of my applications, I have an environment available.

**3:29:35** · And so what does this environment do toml file actually look like? Well, I keep mine pretty simple.

**3:29:42** · All this environment.toml file has is a file that's called scripts/workree/bootstrap.sh.

**3:29:52** · And anytime a new worktree is created, the first thing that happens is that this shell script gets run. And so if I was making one for the creator carousel studio, what I would create is in.codeexc/environment/environment.tottoml, I would have a file that looks like this. And then in a scripts directory, I would have this bootstrap script. Now what this bootstrap script does for me is it basically looks for any dependencies at the root that need to be installed.

**3:30:23** · It looks for any secrets at the root folder for like the main work tree and gets them a local version into the individual work tree. And it also makes sure that any ports for this application don't conflict across work trees. And so the typical workflow which will then occur is you make some changes in a work tree. You create a branch in that work tree.

**3:30:47** · You commit and push and then open up a PR a pull request a request to merge the work in that branch into the main branch. And so you're able then to be working on multiple features at a time which may have some light conflicts with each other but you can sort of worry about resolving them later but you do have to resolve them.

**3:31:09** · So if two work trees are editing the same file sometimes even when they're working on the same file the additions they're making to those files could be such that they don't actually conflict but sometimes one PR changes the foundation underneath another PR. And so when that occurs, it's sort of incumbent on you to think, okay, which ones of these should I merge in first and how should I manage the conflicts between these PRs in order to reconcile them.

**3:31:38** · Now before agent coding like this is something that people did quite often not with work trees but collaborating between different people on big teams of developers and it was a mental exercise that they had to sort of go through line by line and figure out okay how am I going to resolve this but now we have access to this super intelligence that can do this thinking for us and so it's not as much or it's not a huge cognitive

**3:32:07** · cost to reconcile how these inconsistencies with work trees or think about which one should be merged in before another one because the agentic coding tools themselves could help us with that reconciliation. And so if I was like giving human instructions for how to handle conflicts, you would, you know, keep each work tree to one issue, avoid assigning the same files to parallel tracks or like choose your work trees based on the opportunities for parallelization, which is what we tried to set up when we were designating the issues. merge lower risks PR first.

**3:32:37** · But then like again, if you have any confusion about this or you're struggling to get it set up or there's some sort of weird error that's occurring, just ask codeex. It'll solve it. It's really smart. Now, if two changes need to be designed together, like you're designing, I don't know, like the editor for this canvas for this application, and then you're also want to design like what toggles are on that. Obviously, you can't design those on parallel.

**3:33:06** · So you're going to have to stack those as like separate PRs or like one will have to be built first before you can start work on the other.

**3:33:15** · And so for the rest of this course, we're getting close to the finish line.

### Building Creator Carousel Studio

**3:33:19** · Now let's actually see it through and build this application. So it went and did the scaffold of you know and okay and I'll also be actually implementing these work trees where I see the opportunity arise to implement them. So let's take a look here. says it's running. And so one of the nice things here is that you can actually open up things in this web browser. And you can use later this tool called browser use to control the inf browser.

**3:33:47** · So this is like just a sort of outline, but it it looks pretty nice to start. Like it's a pretty good starting point. Okay. So I'm just going to say it looks good to me.

**3:34:03** · create a pull request. All right, the pull request is opened. So, we can click this button to take a look at it. And we'll see that here. I of course I wrote this all by hand. I would never use AI to write a pull request copy. Never do that. It's very unethical. Yeah. And so, wow. Built with compound engineering.

**3:34:26** · Even got Oh, they're really sticking out their property here. Okay. So, again, I'm a dummy. I I'm not calling you guys dummies, but I don't know anything technical. So, the goal here is to build this with like as little brain power as possible. So, you come back to codeex and then you say looks Gucci, please merge. And it's very important that you use these particular words Gucci and PLZ. Doesn't work as well if you say P L E A S E. Codeex responds well to um to that. All right.

**3:34:57** · So we look here and we see that this has been merged in. So if I refresh now, there's no more pull requests. The number of issues has gone down by one. If you click on this pull request thing, Jesus, GitHub's been having a lot of issues. You can see now that it shows up as closed rather than open. So let's come back here and let's just ask codeex now. Great. What should we work on next? All right. So it's suggesting start with four and then the fun split opens up five convex persistence in one work tree.

**3:35:28** · Six SVG and sharp renderer spike in other work tree. So we've been working consistently in this one thread. I'm going to open up here go and start a new work tree.

**3:35:41** · Anyway, uh let's go highowered.

**3:35:44** · uh start working on GitHub issue 4 on a new branch.

**3:35:52** · Boom. So you can see there's this work tree creation process. Right now I haven't set up any environmental toggle.

**3:35:59** · So it should occur relatively fast. All right. So the branch got created. It picked up issue 4 and it's going straight to working on it. Okay. So this got finished after 6 minutes and 23 seconds. So again, we're taking a yolo approach to this.

**3:36:20** · So let's just make sure first can I start this up and can you let's say use concurrently to document how to start up convex and nex.js simultaneously.

**3:36:39** · Okay, cool. Can you start it up now and let me see it in the inapp browser?

**3:36:48** · Okay, so we're able to see it in this work tree now in this inapp browser. I guess this is going to be like some kind of template that we'll be using later.

**3:37:00** · question or actually let's just say do okay and can we make sure those environment variables will be on the main work tree or can we have some sort of uh environment bootstrap in this repo as part of this PR I have a skill to basically automate the creation of those bootstrap scripts for PR RS that I was telling you about.

**3:37:31** · So, let's make sure that that's going to be the case so that we have this environment created. All right. So, we got these shenanigans made. We got a secrets file created. And then, if you recall this environment toml concept that I talked to you about and having a bootstrap file that it runs, that's all created. Um, let's just say this is all good as is. Um, can you kill local port so we can run it here?

**3:38:09** · Something that happens when you make a web application is that the web application when you test it locally has to be running on some port on your computer. So you boot it up and then you can test it out locally. And what we're doing here is clearing the services which are currently running on the port.

**3:38:28** · Run it for me brother and open it up brother with browser use. These tools respond better when you call them brother with a uh ambiguous Eastern European accent. They can sense the accent brother. I don't know what accent would that be. Estonian. I'm going to call it an Estonian accent. All right.

**3:38:52** · So we got like some kind of buttons here for brand kit import events. Okay, that's uh some kind of template here. I guess these are going to be like functionalities we have later down the road. At this point, what should be testable? I don't even know where I'm at with making this application. But the goal here is to use my brain as little as possible because my brain power is extremely valuable and so we don't want to be wasting it whenever I don't have to. Okay. What you can test in the browser. It renders. This thing is static. Okay, that looks good.

**3:39:24** · It looks Gucci, my brother. Why don't we be uh merging it in? And then you tell me what is next thing we can work on. That was much better. When I say merging, I mean the P request. Okay. Wow. Beneos are Morgan. Morgan is my Rico.

**3:39:45** · I mean Merge in the pull request. Oh, that's funny. My editor is going to laugh at that for sure. All right. So, this one is merged in. Um, very good.

**3:39:56** · So, what I'm going to do now is I'm going to say, can you kill the processes? And then I'm going to open a new chat. And I'm going to open this new chat in a work tree. And look at that.

**3:40:10** · Now, we got an environment. We got an environment. Yeah, boy. And now I'm going to say on this work tree I want you to claim issue five and start working on it GitHub and make a pull request. And then over here I'm going to say I want you to claim issue six and start working on it GitHub and make a pull request. So now we're going to be able to have two things that we're working on in parallel.

**3:40:39** · And you might ask, okay, if you're working on both of these things in parallel, how are you going to manage the pull request process? Well, I'm a dumb, stupid idiot with no brain power. But like, this thing, this this computer thingy is really intelligent. So, we're going to ask it. I got work trees started for both issue five and issue six separately. How should I merge them in? like would you recommend doing one before the other?

**3:41:10** · So it says there's no direct dependency between them. They're kind of parallel and so it suggests doing six first and then update rebase five onto main. Rebasing is a git concept to sort of make different branches consistent. Again like you don't need to know what it is exactly if you want to figure that out. The best way to do that is just ask codeex to help explain it to you. If you want to understand it, just ask Codex about it.

**3:41:43** · So, we got this thing going. We got numero synco and then over here we got numeroace, right? That's pretty cool, huh? I mean, in my opinion, we are kind of living the dream here. The dream being to let the machines do all of our work for us and then we just like sit back. Yeah, of course, bro. actually do it and then push your poll request. I don't know. Sometimes these things can be stupid and just stop early for no reason.

**3:42:13** · All right, so I've literally just been sitting here working on other projects for the last 10 minutes and you see this one worked for 11 minutes and then this one worked for 10 minutes. And so if we didn't use work trees, these two things would have you know stacked one on top of each other and would have taken 20 minutes. So we save some time here. So I recall here the advice was to merge number six in first. So let's do that. Ah, sounds good, brother. Let us be merging in the PR number six.

**3:42:44** · I like getting his idea. Or actually the PR number 16, but issue number six. So you still have to choose an order in which to merge in these PRs. And so I'm not going to initiate or actually let me uh let me speed that up. And then after we get five and six merged in. What's good amigo?

**3:43:11** · The issue number can whisper flow. No, not really. Kind of. Okay, good. Amigo, that's pretty funny. Oh, whisper flow has uh some ability to handle Spanglish. This will be good to know for all you Spanglish speakers out there.

**3:43:41** · Let's try uh let's try Russian.

**3:43:46** · Oh, it translated it to like English, but works well enough. Let's see how this one's doing. All right, so this one's done. We can archive this one. We can archive this old one. And we got some random ones just sitting around here. I might as well archive them.

**3:44:02** · Archive. Archive. Okay, here we are.

**3:44:05** · We'll just open up a new one here and say, "Can you help me test out app in its current state in the in app browser?" We'll do a little testy test and then we'll figure out if we're on the right path with like automating the creation of these graphics or what we got to do next. All right. So, it's showing up here and now you can see I asked it to test it out. So, it's actually going and doing these testing activities.

**3:44:36** · You can see the cursor right there over import events itself. All right. So, it says current state looks clean but very shelllike. No errors or warnings. All the tests pass. These main buttons aren't actually wired up yet.

**3:44:51** · Okay, cool. What are the next issues you can work on? Next, I'm going to show you something really crazy. You're going to you're going to enjoy this. All you Vive coders out there, do you see these in GitHub issues? First, I want you to download these Instagram images from this post and store them in here somewhere.

### Letting Codex drive the next issues

**3:45:17** · I want you to have those as a reference of like kind of the type of final product that we're trying to produce. Then I basically just want you to go through these tickets one by one and just keep going until we have some interface that helps me automatically create images of the style that you see in those Instagram images about as pixel perfectly as possible. I just want to get it working as a local web app right now. And then once it's done, we'll work on deployment.

**3:45:48** · So basically what's happening here is that I am feeling really lazy. Like you have no idea how long I've been working on this course for. And so I want to speed up this process to just like yolo it. I'm going to deliver to you a working web app. Okay? I am a keeper of my promises, but I'm getting kind of tired of this. I got other things to do.

**3:46:15** · I can be going outside, seeing things, taking vacations. Instead, I'm here teaching you Codeex desktop app. And so, we need to speed this thing up. And so, what I basically said is, look, I just want you to go straight through all these issues, but this is actually a teaching moment. Okay? So, I'm saying here, download these Instagram images and now you kind of have a source of truth. Like, this is what I want to produce. Okay? And I just want you to go straight through all these tickets.

**3:46:41** · Just don't stop, okay? and just keep going until this thing is done and I can try something out. Now, what's the risk of approaching building something in this way? Well, you might come up with something that's totally off base, but and I wouldn't create all types of software in this way, but this kind of software like maybe I would. I'm not intending this for public consumption.

**3:47:04** · This is kind of like a throwaway fun task for me. I might use it. I have some like events organizing software ideas in the back of my head. And so maybe I would actually use this software, but even still, it's going to be like some throwaway thing for me. And so this might be an appropriate way to build this kind of software. And it's a strategy that you should be aware of too when you're thinking about building your own things.

**3:47:26** · Even if I'm building things for public consumption, this type of strategy that I'm executing right now may be an appropriate way to do things because you can kind of think of software building in this modern agentic era as sometimes being a bit like sculpting except you can like take the pieces that you sculpted off and graft them back on uh costlessly as well. So the sense in which I mean is like about sculpting is that I just let this thing like go straight through non-stop, right?

**3:47:55** · And do its thing, but then maybe there's like I don't want in it though the core functionality is there.

**3:48:03** · So then I like a sculptor, I can just sort of like chip off those little things that I don't want at the end when it's all done. But for now, I'm tired.

**3:48:12** · So I'm going to let this thing just, you know, snap snap. I got apps to make. I got fancy restaurants to go to with all this YouTube ad money, you know, I have to spend it somehow. And so, I'm going to be researching some fancy restaurants that all you people who are viewing this course are going to be paying for. So, I'm going to have my fileman and my my caviar cuz I'm a refined man with refined tastes. All right, let's uh let's see how it goes. All right, so it made something. Let's uh see what it made exactly first.

**3:48:44** · How long was this thing working for? 18 minutes and 5 seconds. Okay. And Huh. Interesting. So, is this what it produces? Not bad. Show me how it works. Let's uh let's see what this thing does. So, like obviously, you know, these proportions. You got to got to work on these. It's like created a 4x4 grid here. Oh, wow. So, it actually it got all of these. Uh-huh. So, you like you put them in over here, I guess.

**3:49:14** · And then you got like different events here. Yeah, that's pretty cool. So you stick your photo in slide field spring.

**3:49:23** · Okay, so you can like edit a particular one here. Not bad. It's like it's not not bad at all. Obviously room to improve on the design direction both in terms of the user interface and like this particular thing. But I kind of like it. So, if I was like continuing to work on this, and I'll work on it a little bit more here, but these things are kind of like getting outside the scope of what I want for this beginner course.

**3:49:51** · There are very interesting possibilities now with how you can design front ends, skipping, you know, some step of making Figas, for example, and going directly to highfidelity mockups using the image gen functionality that I think I've already shown you guys. Sweet. So, I can click on this for export PNGs and then I guess I can open it up. How does that work? I clicked export PNG but not able to open anything up when I click on it. Now look at this.

**3:50:24** · This is really cool. So you just take a screenshot here and just paste it right in. Very handy. I'm telling you like the codeex desktop app is next level. Um just right now I was reading this like very interesting tweet. The agent harness is the platform. Multi-billion businesses will be built on top of codeex co-work cursor. I don't know about co-work sucks. And cursor I mean they are they're dead in the water. Same as they were with AWS Azour GCP.

**3:50:55** · Now is the time to invest. Thank me later. All right. I have to fix these links and I guess they do open up now. So you can go back and let's just go here and I can click on this. Let's see. Export PNGs.

**3:51:13** · There you get it like that. Downloaded, I guess. Just click on it. Cool. Don't look perfect, but don't look terrible.

**3:51:19** · Okay, cool. Let's make what are the remaining issues to work on? What's the exact order in which you would want to do these? Okay, great. I want you to keep going through in your suggested order until everything is done and we're like producing output that looks like the sample output. You do have the sample output, right? Like the ones from the Winnipeg Digest. Yeah. By the way, I just want you to keep going.

**3:51:48** · Like, don't stop. Just keep keep going all the way through to the end because I'm really freaking lazy and I don't want to keep working on this project no more. So, you got to help me out. You feel me? Telling you, communicating in this way, it's been scientifically proven to get better results out of LLM.

**3:52:07** · I'm writing the paper right now, but it's uh it's in stealth. We're not uh we're not letting the public know just yet. This is just between us. See, telling us that it feels us. All right.

**3:52:18** · So, I just let it keep going. It worked for 15 minutes and 21 seconds, and it says here's what it produces now. So that's like everything that it's producing. Here's an example image. Like that looks pretty freaking good. And then this is the reference. Okay. So like here's what it produced and here's a reference. Like obviously there's room here for improvement. I don't have access to that proprietary logo. But for my purposes, for how this is working locally, this is amazing.

**3:52:48** · Like do you know how lazy I've been in the last 15 minutes? Just been on my phone like reading Twitter tweets while stuff is going on here. It's awesome. All right. Very nice, my brother. I am mucho proud of you. I cannot underemphasize how proud I am of you. Last step because I am lazy I want you now.

**3:53:12** · Please, I beg of you, my brother. I want you now to deploy this on real website.

**3:53:18** · A real website on Versel. Please my brother, I beg of you. It is very important that you do this and you connect it to convex as well. Thank you, my brother. You you mean the world to me. I'm telling you, you just put a little bit of pizzazz into how you're talking to these things and and they know. So, it's going to just set everything up, right? We got Versel already connected. We got like convex connected.

**3:53:44** · And so, now we just let it do its thing for us, right? like take me out of the picture and just get the deployment working. All right, done my brother. It is live. Let's check it out.

**3:53:58** · Damn. Well, would you look at that? That is pretty freaking cool if I must say so myself. I mean, kind of confusing. Like could uh improve the interface, but let's try using it out. Let's like find a new set of events and populate them, you know.

**3:54:16** · Very cool my brother overall I am wanting you to try to update uh this this thing you have here why do not we being trying to find events in Aston Illinois if you know where this is so you'll be looking up the events in Aston Illinois and I am wanting you use our skill we create in this repository to be updating what I see on the website. I'm sorry, guys.

**3:54:48** · I know that this must be very irritating to hear all my different uh accents, but look, how how long can this course go? I don't know how these other course creator people do it. Saw this one he made a 10hour claude code course. Now, in reality, he just filled it with absolute nonsense for like 9 hours. And I guess he had something to say for 1 hour, right?

**3:55:16** · But it's pretty hard doing these long courses and I bet nobody's actually listening through until the end anyway.

**3:55:24** · But if any of you do, please leave a comment on how you like my accent. Okay, my brother has updated it. So, it used I guess some carousel intake skill that we've created here. If you go here now, it's got a bunch of Evston events. So, Evston digits downtown Evston Farmers Market. The images don't line up though.

**3:55:49** · For the ones for which you can find images, can you get those to line up as well? The images don't look the same.

**3:55:55** · Why is it doing it in Spanish? It's totally bizarre. Apologies to all the non-speakers.

**3:56:02** · Oh, yeah. Also for the ones for which you don't find um like good images, you can use image genen to generate some images. All right. Somehow it changed languages again. Mucho loento paral anglo parantes very sorry for the English speakers.

**3:56:25** · I love speaking Spanish with a very strong gringo accent but doing it perfectly grammatically well. It's kind of like um I don't know just like flipping out an Indian accent every now and then. Russian accent. I think more economists should learn accents. that would have kept me awake in more macroeconomics classes if uh some of my professors just, you know, put on their, you know, strong strong Colombian accent. Actually, let's just see.

**3:56:55** · Can you talk to me in Russian only until I say otherwise?

**3:57:06** · I'm really just uh trying to get this thing done right now, aren't I?

**3:57:12** · All right, let's keep going. What do you say, Alexi? Are you watching this far into the video? Damn, that's pretty cool. Going to speak Russian in Codeex, too. I thought about using Codeex as a language learning tutor. Actually, that could be a fun way to do things is just have it, you know, speak to me in Russian all the time. Wow, that would be that is a very interesting idea.

**3:57:40** · And you could even have it like use an 11 Labs voice so that you can listen to it. Huh.

**3:57:51** · There is something here. That would be an interesting form of multitasking. I may actually do that cuz I speak Spanish pretty well. I want to improve my Russian. I want to improve my Portuguese. Those are kind of highest on my list.

**3:58:11** · Sublvator maiden art center farmers market black experience injustice pilgrim.

**3:58:22** · All right, this is actually pretty good.

**3:58:23** · So what it says here in Russian is generate some images through image gen. And so it's like actually making the correct images, I guess, to match like what should be going in these carousel things. So just going to let it do its thing.

**3:58:49** · No idea how long this is going to take, but you know, we don't use our brains here cuz my brains used on more important things like uh reading Twitter. You know, that's what I got to use my brain for. All right, so it finished. We come in here. We see that image generated a bunch of images. Kind of tested it out. Didn't get all of them. It was taking forever and I am ready to eat dinner. So, decided to shut it off. But if we take a look here, we see we've got, you know, this right here.

**3:59:20** · I can do this to export PNGs, I guess. And if I am lucky, so which one is this? Event two. Let's take a look at that. Downtown Evston's farmers market. I dig it. So, it's a little bit annoying that I have to like click this button again to get it to work, but let's open it in a new tab like that. Well, that's cool. Friday nights at the Dearborn Observatory. That looks like an event that I would like to attend. Wouldn't you like to attend?

**3:59:53** · We're going to go 900 p.m. to 11:00 p.m.

**3:59:55** · May 1st. Be there or be square. All right, guys. That was the course we took you from never having done anything in codeex before in your life. You were just, you know, working with chat GPT and now you know how to build out full-blown web apps with a product builder mindset, whether for your own projects, for client work.

### Course wrap-up and next steps

**4:00:20** · You can just go on Upwork right now with what I've taught you here and you have the ability to generate, you know, a four figure a month side hustle just off this course.

**4:00:34** · Now, if you want to get continued advice from me on different things that you're learning in the AI space, whether codec or otherwise, come in here and join the AI MBA. So, we got people in here all the time learning all sorts of different things. This guy was frustrated with Codeex. I was trying to help him out.

**4:00:54** · This guy is seeing some potential problems with Claude and so I was helping him out with that. Nick is building an internal operating system for his local newsletter and I gave him my advice on what that infrastructure should look like. So if you guys want to keep up with the cutting edge on AI, you can check out the free group.

**4:01:12** · Additionally, if you want to get on weekly calls with me, you can join the AI MBA Pro where we meet as a group, keep up with our particular goals, and all push each other to get better with AI in whatever respect that may be. And if you join the AI MBA Pro, I have some special tutorials. So, I have here, for example, an update to my clawed code course with the things that I recommend now. And the group calls are all here.

**4:01:41** · And all these transcripts of the calls you can access via an MCP server that I've set up. Finally, I know a lot of you who are following me are economists.

**4:01:51** · So I also do economic specific workshops on how to use agentic coding tools like codeex or claude code for research purposes. So if that's something that interests you, send me an email at uni@contentquant.io or unicate-ba.io io and I'll be sure to get back to you.

**4:02:12** · That's it for today.

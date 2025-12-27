# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything.** And it's way better than their apps.

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Problem We All Know Too Well

Tell me if this sounds like you because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. 

And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works. At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

The fundamental issue is that browser-based AI traps you in a limited environment. That response is just words. And if words are what you want, you're doing fine. But what if you want to do something? What if you want to cause effects out in the world? What if you need access to your files, your data, your actual work environment?

There's a better way to do this. Hear me out. It's in the terminal.

## Understanding AI's True Nature: It's Good People, Bad Software

Before we dive into the terminal tools, you need to understand something crucial about AI. As Jeremy Utley from Stanford puts it: "I joke. AI is bad software but it's good people." This changes everything about how you should approach it.

AI is like "a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back." AI wants to be helpful and is predisposed to say yes. It's been programmed to be a "helpful assistant," which means if you aren't careful, AI will gaslight you.

Here's the thing: AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

The solution? Always instruct the AI: "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

When you realize you're dealing with good people but bad software, it changes how you approach it. You ask for volume, you iterate, you ask it to try again, and you ask it to reconsider.

## Getting Started with Gemini CLI (It's Free!)

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free. You can install it with one command. Go ahead and launch a terminal - it doesn't really matter where you launch it. Mac, Windows, Linux, all these terminal apps work everywhere.

For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux. We'll copy and paste this command:

```bash
# Installing Google Gemini CLI
curl -sS https://storage.googleapis.com/gemini-cli/install.sh | bash
```

If you run into a scary issue, run it with sudo. And if you're on Mac, you can also use brew:

```bash
brew install gemini-cli
```

Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account. It's going to open your browser, sign in, and you're logged in.

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" And then it responds just like we're used to.

## The Terminal's Hidden Superpowers

But notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

It's asking us a question: Do you want me to write a file for you? Yeah, dude. Go for it.

This thing can do everything a browser can do, but it has a superpower. **It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. Look, it actually made files on our computer. There they are.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on.

Let's take a look at it:

```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. And every time you launch Gemini, it's going to load that file as its context.

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file. And I'll tell it this: "Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about. Look at that. I didn't give it any context. It just knew. This is a new chat session.

## Context Engineering: The Foundation of AI Mastery

What we just demonstrated is basic context engineering. Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, "Absolutely. Here's a compelling email," and they'll write it immediately. Most people then say it sounds like AI, it doesn't really sound like me. But have you told it what you sound like?

Context engineering is telling AI what you sound like. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer" that also references our product specifications.

Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind. All of the stuff that are implicit, you actually have to make explicit.

The simplest test for context engineering is the test of humanity: Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## Taking Control of Your AI Workflow

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

When I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

I'm literally using the `gemini.md` file right now for this project. This is a small example. Let me show you a big one. This is the `gemini.md` file for this video. It tracks everything. It describes how I create project status, major decisions I made, even other documents it should look at.

## Claude Code: The Daily Driver

Now, I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy. I use Claude Code, which is Claude in the Terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**.

Look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

Let's get it installed with one command:

```bash
npm install -g claude-code
```

And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of AI Agents

Again, don't be afraid. Ask Claude a question like, "I need to find a NAS for my house. Here's my budget, what I want to do. Create a report for me." And just like Gemini, it does have some fun little messages for us. It will search the web.

And it can also have a context file, too. If I run that same command `/init`, it will create what's called a `claude.md` file. Noticing a trend here. And it's doing the same thing, looking through our project, trying to figure out what's what, and creating a context file.

But what's funny with Claude, that doesn't really matter too much as long as you know how to use their most powerful feature: **agents**.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a home lab research expert. Create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. We'll do just this project.

## Why Agents Are Game-Changers

Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

He's giving him a fresh set of instructions and get this, **a fresh context window**. You saw just now we have 200,000 tokens in our context window. We use 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

Claude just delegated this task to a new agent. He's got a fresh pot of coffee. He's ready to go. He just walked into work.

## Advanced Prompting Techniques That Change Everything

Let me share some advanced techniques that will transform how you work with AI. These come from Stanford's practical AI research and will make your terminal AI experience even more powerful.

### Chain of Thought Reasoning

One of the most powerful techniques is getting AI to "think out loud." This is called chain of thought reasoning. When you get an AI to think out loud, it meaningfully improves the outputs of the model.

How do you do it? Add one sentence to whatever prompt you've given: "Before you respond to my query, please walk me through your thought process step by step."

Why does this work? A language model doesn't premeditate a response. It's thinking one word at a time. When you see text scrolling in ChatGPT or Gemini, that's not some clever UX hack - that's literally how the model works. But when you ask it to think out loud first, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

### Few-Shot Prompting for Perfect Outputs

AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. Few-shot prompting means giving AI quintessential examples of the kind of output you want to receive.

For example, what are your five greatest hits of emails that you're really proud of? Include those emails in your prompt. If you don't give any guidance, it's going to sound like whatever it thinks the average response should sound like, and most of the time its intuition is wrong.

Bonus points if you give a bad example too: "Please follow this good example and steer clear of this bad example." Using real examples is much better than using adjectives.

### Reverse Prompting: Let AI Ask the Questions

This technique involves asking the model to ask you for the information it needs. Instead of AI making things up, you give it permission to ask questions.

Add this to your prompts: "Before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then, instead of writing with placeholder text, it'll say, "I'm going to need the most recent sales figures to be able to write this email."

This is part of treating AI as a teammate, not technology. Any good manager tells their employees: "If you have any questions, don't hesitate to ask me." But AI, in its desire to be helpful, doesn't want to trouble us with questions unless we give it permission.

### Role Assignment for Focused Expertise

Assigning a role is one of the most foundational techniques because it tells the AI where in its knowledge it should focus. Simply saying "you're a teacher," "you're a philosopher," or "you're a molecular biologist" triggers deep associations with knowledge.

Better than just a generic role is being specific: "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this correspondence?"

## Running Multiple AIs Simultaneously

Let's get crazier. I'll create another tab because no one can stop us. Jump into our project. Launch Claude in dangerous mode. And what do you say we have Claude use Gemini for research? Yes, because we can run Gemini and Claude and all these terminal tools in headless mode, meaning you don't jump into a TUI. You just run them with one command.

It's like `gemini -p` and then here's your prompt. We can just create an agent that does that. There's the prompt. We're having an AI use an AI right now.

## Advanced Features and Customization

Claude Code has a feature called output styles. Look at this `/output-style`. We got a few defaults in here. And these essentially control the system prompt for Claude code. How it's going to respond to you, the persona it has. The default is code and that's what we're using. But we can change that.

Let's create a new one. You are a home lab expert designed to help me create the best home lab possible. You can create output styles that are tied to just your project or as a whole. Whatever project you jump into, you can switch to those output styles.

I'm using the output style right now to make this video. Script writing output style. And this is what it looks like. It's pretty intense. Optimized for what I do.

## Using Multiple AIs in Perfect Harmony

Here's the thing. I don't just use Claude code. I use Gemini. I use Claude code and I use Codex which is ChatGPT's terminal tool all at the same time. Let me show you how.

Gemini, Claude code, ChatGPT's Codex. I'm using all three right now to work on this video script. How? Two steps. First, as long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

And I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle. Write it to `discovery-hook.md` and then I'll have Codex review it.

They're all using the same context, different roles. I mean, I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory. That's awesome.

## Roleplay Training: Your AI Flight Simulator

One of the most powerful applications of terminal AI is using it as a flight simulator for difficult conversations. You can practice salary negotiations, performance reviews, or any challenging interaction before the real thing.

Here's how it works: Set up three different chat windows. One is a personality profiler, another is the character of the individual you need to speak to, and the third is a feedback giver for objective evaluation.

Start with the personality profiler. Describe the person you need to have a conversation with - their communication style, background, and the situation. The AI will create detailed instructions for roleplaying that person.

Then open a new chat window and paste those instructions. Now you have an AI that will realistically simulate your conversation partner. Practice the difficult conversation, trying different approaches and responses.

Finally, take screenshots of your practice conversation and upload them to a third AI window trained to give feedback. It will evaluate your performance, suggest improvements, and help you prepare talking points for the real conversation.

This is the first time in history you can get realistic practice and feedback for specific difficult conversations before they happen. It's like having a flight simulator for human interaction.

## Taking Back Control of Your Data

Now, are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive. I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.

And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock in so I can't leave. No, I reject that. **I own my context**. If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

## Understanding the Architecture Behind the Magic

What's really happening under the hood is something called the Model Context Protocol (MCP). And this really is a big deal, but most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

Here's how it actually works. We're building what's essentially a microservice architecture. In MCP terms, your terminal AI tool is called the host application. The host application uses the MCP client library to create an instance of a client. Out there in the world, we have MCP servers - these could be servers that already exist that somebody else has built, or servers that we ourselves are creating.

Inside each server, we have access to tools, resources, prompts, and capabilities that the server makes available and even describes to the outside world. This is a server process with a URL, port, and a variety of well-known RESTful endpoints described by the MCP specification.

The connection between client and server can be standard IO for local processes, or HTTP with Server Sent Events for networked communication. The messages being exchanged are in JSON RPC. There's protocol for a client announcing itself to the server and establishing communications, plus ways for servers to send asynchronous notifications back to the client.

This architecture gives us huge benefits: pluggability, discoverability, and composability. These servers are composable too - a server itself can be a client of another server. So if you need to consume from a Kafka topic, your server can connect to a Confluent MCP server instead of writing all that Kafka code yourself.

## My Daily Workflow System

I want to get real practical. I want to show you exactly how I run a project like this. How I keep things in sync, how I keep my Claude, Gemini, and agents files in sync and work on a daily basis using a system like this.

First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex. I rely on Claude to run my agent that will close out everything. So, I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." Run my agent script session closer.

This is one of those agents I keep as a personal agent. I use it for many projects. And these agents are just files. They're files inside an agents folder. But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions.

It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents. And then this is probably my favorite part. **I commit my project to a GitHub repo**.

So, normally you would use git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So, I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. That's the power of using GitHub with all your ideas.

## Building Your Personal AI Critics

This is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things. So, when I'm really tired at the end of the day and like I've been working on a video and my mind is fried, I'm like, "Okay, tell you what, I'm done. Close this out."

It will look through all this stuff. It will figure out where I'm at, end the project, end the day, where I need to be, and then I can start fresh the next day and be like, "Hey, where we at? What are we working on?" It can tell me, "Hey, Chuck, you finished the script. It's time to record. We made these three decisions. Go for it."

Now, I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. So, here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean.

So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it." I wanted something to be super mean. I wanted to be hard to please. So, that when it did tell me I did a good job, I knew it. Like, it was good.

## The Open Source Alternative

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called **OpenCode**. We can install it with one command:

```bash
npm install -g opencode-cli
```

That was quick. If I can just launch `opencode`. You can open and close your terminal. This is OpenCode. A nice terminal user interface. They launched us straight into Grok code fast one. They have a deal with Grok AI that allows you to use this for free for a while.

We can use local models. This is the killer part. I don't think any other tool does this. I can switch models midway. Let's go back to Grok. What's our next step? While it's doing that, I can do new session. This is a new session. Push models to Claude.

We can also share these sessions `/share`. This is so crazy. The URL is copied to my clipboard. So, I can go to my browser, paste that URL in, and I can share your session with people. That's awesome.

## Building Your Own AI Superpowers

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

And this is just one tool I've made. Look at the other stuff I've done. That crazy project I showed you in the beginning was running like seven agents. This is a custom-built project just with Claude code. And I'm going to use it right after I record this. It's going to go through every file. It's going to transcribe it, read it, and give my editors notes they need to be able to edit this video.

Seriously, the tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

## The Coaching Mindset: Your Key to AI Mastery

Here's the crucial insight that changes everything: The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

If you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence. AI demonstrates 100% of the predominant human biases. When you realize you're dealing with good people but bad software, then it changes how you approach it.

You ask for volume and you iterate. You ask it to try again and you ask it to reconsider. You become a coach, not just a user.

## The Adjacent Possible: Expanding What's Imaginable

As Nobel Prize-winning economist Thomas Schelling said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him." If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

In innovation studies, this has been called the adjacent possible for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible.

Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally.

## Why This Changes Everything

So, how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone. Everyone should be using this. Like, make everyone use this. I'm going to make my kids use this.

This is really a gateway to building true agentic AI in the enterprise, in a professional setting. Instead of being limited to just getting words back from an AI, you can cause effects out in the world. You can integrate with databases, APIs, file systems, and any other resources your work requires.

The architecture is pluggable and discoverable. You don't need to know very much about what a tool does - you just plug it in, and your AI can discover its capabilities and use them. This creates a composable system where servers can be clients of other servers, building complex workflows that would be impossible in a browser interface.

Seriously, nothing is stopping you from trying this right now. Gemini CLI, that's free. OpenCode, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. Like, you saw all those features. I use that every day, dude.

Just you got to try it. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower and build whatever you want.

The terminal isn't scary - it's your gateway to taking back control of AI. While everyone else is stuck copying and pasting between browser tabs, losing context, and fighting with scattered notes, you'll be running multiple AIs simultaneously, maintaining perfect context across sessions, and building custom agents that work exactly how you need them to.

Your projects will live on your hard drive, not locked in some company's chat interface. You'll own your data, your context, and your workflow. And when the next breakthrough AI comes along, you'll be ready - because everything you've built works with files and open protocols, not proprietary chat windows.

Perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind. The techniques are there, the tools are available, and your imagination is the only limit.

So get your coffee ready, fire up that terminal, and join me in the place where AI actually gets work done. Trust me, once you see what's possible, you're never going back to the browser.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-27 09:23:09

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,205,300
   - Comments: 4,136

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 633,598
   - Comments: 816

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 475,065
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 30,081
- Total Output Tokens: 17,668
- Total Tokens: 47,749
- **Total Cost: $0.3553**
- Model: Claude Sonnet 4


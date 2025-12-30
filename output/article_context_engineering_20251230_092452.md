# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Trap We're All Stuck In

Tell me if this sounds like you, because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

The fundamental problem is that browser-based AI locks you into isolated conversations. Each chat exists in its own silo, and when you need to bring external data or tools into the conversation, you're stuck with manual copy-pasting. The response is just words - and if words are what you want, you're doing fine. But what if you want to do something? What if you want to cause effects out in the world?

## Getting Started with Gemini CLI (It's Free!)

We're diving straight into the terminal, and I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation is Dead Simple

Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux - all these terminal apps work everywhere. We can install it with one command:

```bash
# For most systems
curl -s https://packagecloud.io/install/repositories/google/gemini-cli/script.deb.sh | sudo bash
sudo apt-get install gemini-cli

# For Mac
brew install gemini-cli
```

If you run into a scary issue, run it with sudo. Never chucked our coffee.

Before we launch it, we're going to make a new directory:
```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Superpowers Begin

Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" 

That wasn't so bad, was it? But notice some superpowered things:

1. **We got Gemini 2.5 Pro** - the latest and greatest model
2. **Context visibility** - "99% context left" - every chat you have with AI has a context window. The browser hides it from you. The terminal does not.
3. **File system access** - your browser can't do this next part

Watch this magic happen:

> I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources, and then compile the results into a document named best-coffee-method.md and then create me a blog plan, just an outline. I'll do the writing.

It's asking us: "Do you want me to write a file for you?" 

Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. Look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changer: Context Engineering

If we type `//tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal.

Type in `//init`. Just like that.

What it's doing right now is something powerful. **It's creating a gemini.md file. And in the process, it analyzed our project, read our folder, read our files.** What it just did there was create instructions for itself, context for what we're working on.

Let's take a look: `cat gemini.md`

While we didn't do much in this project, it knows what's going on. And **every time you launch Gemini, it's going to load that file as its context.**

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context, 100% left. Notice it's using our new gemini.md file.

"Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about.

**I didn't give it any context. It just knew. This is a new chat session.**

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just have this one file that helps keep us organized. Everything you need. You're never paralyzed again.

## Claude Code: The Daily Driver

I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why: **It has a feature that changes the game. Agents.**

Look at this - I have seven agents performing tasks right now in one terminal. Actually, there's 10. And that's just one of the seven features it has that keeps me glued to the terminal.

Now, Claude Code is not free, but I do have good news. **If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it.** So yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installation and Setup

```bash
npm install -g @anthropic-ai/claude-code
```

Then launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

Just like Gemini, it can create a context file too. If I run that same command `//init`, it will create what's called a claude.md file. Noticing a trend here.

## The Power of Agents

Let's make a Claude agent right now. It's really simple. We'll do `//agents`. We'll get a terminal menu and let's create a "home lab research expert."

Create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on, or personal agents that are tied to everything. You can always call them.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'm going to give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made.

**Watch. It's going to use the home lab guru agent.**

Here's why this is amazing - actually kind of insane. So Claude was like, "Cool, I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

**He's giving him a fresh set of instructions and get this - a fresh context window.** You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated.

I can give tasks to other sub-agents and never have to leave this conversation. Claude just delegated this task to a new agent. He's got a fresh pot of coffee. He's ready to go. He just walked into work.

### Understanding AI Agents: The Autonomous Revolution

What makes these terminal agents so powerful is that they're true AI agents - systems that can reason and act autonomously to achieve goals. Unlike a chatbot that only responds one prompt at a time, AI agents run autonomously through multiple stages: they perceive their environment, move through a reasoning stage to determine the next best steps, act on their plan, then observe the results and continue the cycle.

These agents can work in all sorts of roles. They could be your travel agent to book a trip, your data analyst to spot trends in quarterly reports, or perform the role of a DevOps engineer detecting anomalies in logs, spinning up containers to test fixes, and rolling back faulty deployments. **AI agents are typically built using large reasoning models** - specialized LLMs that have undergone reasoning-focused fine-tuning.

Unlike regular LLMs that generate responses immediately, reasoning models are trained to work through problems step by step, which is exactly what agents need when planning complex multi-step tasks. Every time you see a chatbot pause before responding by saying "thinking," that's the reasoning model at work, generating an internal chain of thought to break down a problem step by step before generating a response.

## The Architecture Behind the Magic: Understanding MCP

What makes all this possible is something called the Model Context Protocol (MCP). And this really is a big deal, but I think most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

**MCP standardizes how applications provide context to LLMs.** For large language models to be truly useful, they need to interact with external data sources and services and tools. Instead of developers having to build one-off connections for each new tool, MCP provides a standardized way for AI to access your systems.

Here's how it works: You have a host application (that's your terminal AI tool) that uses an MCP client library. Out there, you've got MCP servers that provide access to tools, resources, prompts, and capabilities. The connection between client and server can be standard IO for local processes, or HTTP with Server Sent Events for remote connections.

Think of it this way - instead of baking all functionality into your agent, you have pluggable, discoverable, and composable services. The server describes its capabilities to the client, and the client can interrogate those capabilities and use them as needed.

Let's say you're building a service for making appointments. You need calendar integration, restaurant reservations, location data - all these different resources and tools. With MCP, you don't have to build all that into your agent. You can plug into existing MCP servers that provide those capabilities.

The workflow goes like this: A prompt comes in ("I want to have coffee with Peter next week"), the application asks what capabilities are available, gets a list of resources, asks the LLM which resources it needs, retrieves that data, and then uses it to inform the next prompt. For tools, the LLM can actually recommend which tools to invoke and with what parameters.

**This is a gateway to building true agentic AI in the enterprise, in a professional setting.** It's not just about enhancing a desktop application - it's about creating systems that can actually do things in the world.

### The Power of RAG and Vector Databases

Behind many of these terminal AI tools is another crucial technology: RAG (Retrieval Augmented Generation) powered by vector databases. In a vector database, we don't store raw data like text files and images as blobs of data. We use an embedding model to convert that data into vectors - essentially long lists of numbers that capture the semantic meaning of the content.

The benefit is that in a vector database, we can perform searches as mathematical operations, looking for vector embeddings that are close to each other. This translates to finding semantically similar content. RAG makes use of these vector databases to enrich prompts to an LLM by retrieving relevant information and embedding it into the prompt context.

For example, I can ask a question about company policy, and the RAG system will pull the relevant section from the employee handbook to include in the prompt. This is part of what makes terminal AI tools so powerful - they can access and reason over your local files and data in ways that browser-based AI simply cannot.

## Running Multiple AIs Simultaneously

Here's the craziest part about this. Everything I'm doing, talking with these three different AIs on a project, it's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context - it's mine. And that's the difference.

**Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive.

I will use all AI. I will use the best AI. No one can stop me.

### My Multi-AI Workflow

Gemini, Claude Code, ChatGPT's CodeX - I'm using all three right now to work on this video script. How? Two steps:

1. **Same directory** - As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project.

2. **Synced context files** - I make sure my context files are all synced up. They all say the same thing. So gemini.md, claude.md, and agents.md, which is what CodeX uses, and they're trying to make it a standard - they're all the same.

I'll tell Claude to write a hook for this video, authority angle, write it to authority-hook.md. I'll have Gemini write a hook on a discovery angle, write it to discovery-hook.md, and then I'll have CodeX review it.

**I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work.** They're all using the same context, different roles. I mean, I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory. That's awesome.

## My Real-World System

This video was made with this process. Let me show you exactly how I run a project like this, how I keep things in sync, how I keep my Claude, Gemini, and agents files in sync and work on a daily basis.

### The Session Closer Agent

When I'm done for the day, I'll go, "Hey, let's close this out." Run my agent - script session closer. This is one of those agents I keep as a personal agent. I use it for many projects.

It does a lot of stuff, but some key things:
- Gathers everything we talked about, everything we did, and does a comprehensive summary
- Updates a session summary file specific to updating what were some things that were done in past sessions
- Sees if any core project files need to be updated
- Updates every context file: Claude, Gemini, agents
- **Commits my project to a GitHub repo**

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change, so I can see a history of why, what I did and why I did it. Maybe something breaks, I can go back to that change and reinstate it. **That's the power of using GitHub with all your ideas.**

This is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things.

### The Brutal Critics

I don't really use these AI terminal tools to help me create. **I use them to critique me and make me better.**

I got the brutal critic. I told him to be mean. So I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh Chuck, best thing you ever wrote." I'm like, "You're gaslighting me. Stop it."

I wanted something to be super mean. I wanted it to be hard to please. So that when it did tell me I did a good job, I knew it. Like, it was good. And that's what this thing does.

The brutal critic has three personalities or three people that come in and roast it from different angles. **Doing stuff like this saves me hours.**

It's not writing for me. I'm doing the writing because I like to keep that. I think that's important now with AI, but I do have AI roast me, help me stay on track because I get distracted.

## Open Source Alternative: OpenCode

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick.

```bash
# Install OpenCode
npm install -g opencode
```

A couple things real quick. They launched us straight into Grok Code Fast One. They have a deal with Grok AI that allows you to use this for free for a while.

**We can use local models. This is the killer part. I don't think any other tool does this.**

You can log into Claude with this command: `opencode login`. You can choose Anthropic with your Claude Pro. And now I'm logged into Claude Code. I can switch models midway. **All our files are local. Doesn't matter what tool we use. It's all ours right here.**

This flexibility is crucial because it means you're not locked into any single provider. The underlying MCP architecture ensures that your tools, resources, and capabilities remain accessible regardless of which AI model you're using. It's pluggable, discoverable, and composable - exactly what you want when building professional AI workflows.

### The Future: Mixture of Experts and Beyond

The terminal AI tools we're using today are just the beginning. Many of the latest models use something called Mixture of Experts (MOE) - a technique that divides a large language model into specialized neural subnetworks. It uses a routing mechanism to activate only the experts it needs for a particular task, then performs a merge process to combine the output from different experts into a single representation.

This is a really efficient way to scale up model size without proportional increases in compute cost. Models like IBM Granite 4.0 series can have dozens of different experts, but for any given token, they'll only activate the specific experts they need. While the whole model might have billions of total parameters, it only uses a fraction of those active parameters at inference time.

Looking even further ahead, the goal of all the frontier AI labs is ASI - Artificial Super Intelligence. It's purely theoretical at this point and doesn't actually exist. Today's best models are slowly approaching AGI (Artificial General Intelligence), which would be able to complete all cognitive tasks as well as any human expert. ASI is one step beyond that - systems with intellectual scope beyond human level intelligence, potentially capable of recursive self-improvement. An ASI system could redesign and upgrade itself, becoming ever smarter in an endless cycle.

## Why This Changes Everything

So how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel, because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

I mean, I know it's kind of intimidating if you're not used to working in the terminal. **If you can get past that, this tool is for everyone. Everyone should be using this.**

The broader vision here isn't just about making your current AI interactions faster - it's about enabling true agentic AI that can actually do things in the world. When your AI can access files, run scripts, connect to databases, consume from Kafka topics, make API calls, and coordinate with other AI agents, you're not just chatting anymore. You're orchestrating intelligent systems that can cause real effects.

**Nothing is stopping you from trying this right now:**
- Gemini CLI - that's free
- OpenCode - you can run local models if you're worried about that
- Claude Code is paid, but it's overpowered

You will feel like you have a superpower and build whatever you want.

The point I want to hit home is that **I made this for me. This is my own personal software, exactly my use case. What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

**Leaving the browser, going to your terminal, puts you back in control, and it gives you better features.** You got to try it. Dip your toe in the water. It's fine. It's awesome.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-30 09:24:52

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,222,161
   - Comments: 4,173

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 634,844
   - Comments: 818

3. [7 AI Terms You Need to Know: Agents, RAG, ASI & More](https://www.youtube.com/watch?v=VSFuqMh4hus)
   - Channel: IBM Technology
   - Views: 703,304
   - Comments: 515

**Cost Summary:**

- Total Input Tokens: 24,135
- Total Output Tokens: 13,259
- Total Tokens: 37,394
- **Total Cost: $0.2713**
- Model: Claude Sonnet 4


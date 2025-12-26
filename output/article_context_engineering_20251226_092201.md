# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. Each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects, working in the terminal is a superpower. I'm about to show you why. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Problem with Browser-Based AI

Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

The fundamental issue is that browser-based AI gives you just words. And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools.

## Understanding AI Agents: The Foundation

Before diving into the tools, let's understand what makes these terminal AI systems so powerful. We're dealing with **AI agents** - systems that can reason and act autonomously to achieve goals. Unlike a chatbot that only responds one prompt at a time, AI agents run autonomously through multiple stages.

First, they perceive their environment. Then they move to a reasoning stage where they look at the next best steps forward. After that, they act on the plan they've built through reasoning, then observe the results of that action - and around and around we go.

Agents can work in all sorts of roles. They could be your travel agent to book a trip, your data analyst to spot trends in quarterly reports, or perform the role of a DevOps engineer detecting anomalies in logs and spinning up containers to test fixes and rolling back faulty deployments.

## The Architecture Behind Terminal AI

When you use AI in the terminal, you're essentially building an agent - think of it as a microservice. In technical terms, this is called the host application, and it uses something called the **Model Context Protocol (MCP)** to create a client instance.

MCP standardizes how applications provide context to large language models. For LLMs to be truly useful, they need to interact with external data sources, services, and tools. Instead of developers having to build one-off connections for each new tool, MCP provides a standardized way for AI to access your systems.

Out in your system, there are MCP servers that provide access to tools, resources, prompts, and capabilities. These servers make their functionality available and even describe themselves to the outside world through well-known endpoints. The connection between your terminal client and these servers can happen through standard input/output or HTTP with Server Sent Events, using JSON RPC messages.

**This architecture gives you pluggability, discoverability, and composability** - huge benefits that browser AI simply can't match. Instead of baking all functionality into one locked system, you get modular, discoverable tools that you can plug in and combine as needed.

## Getting Started: Gemini CLI

Let's start with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**. I'll show you Claude Code in a second - that's my favorite by far, overpowered. But they share a lot of the same concepts.

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux, all these terminal apps work everywhere.

```bash
# Install Gemini CLI
curl -fsSL https://get.gemini.com/install.sh | sh
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

## The Superpowers Begin

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

It's asking us a question: Do you want me to write a file for you? Do you want me to create a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. Look, it actually made files on our computer. There they are.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changer: Context Files

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, **context for what we're working on**.

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file. And I'll tell it this: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

**I didn't give it any context. It just knew. This is a new chat session.** And as I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project.

I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, **no more 20 scattered chats**. We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

When I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

## Claude Code: The Daily Driver with Reasoning Models

I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

Let's get it installed:

```bash
npm install -g @anthropic-ai/claude-cli
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

What makes Claude Code particularly powerful is that it's built on **large reasoning models** - specialized LLMs that have undergone reasoning-focused fine-tuning. Unlike regular LLMs that generate responses immediately, reasoning models are trained to work through problems step by step, which is exactly what agents need when planning complex multi-step tasks.

The reasoning model is trained on problems with verifiably correct answers - math problems or code that can be tested by compilers. Through reinforcement learning, the model learns to generate reasoning sequences that lead to correct final answers. Every time you see a chatbot pause before it responds by saying "thinking," that's the reasoning model at work, generating an internal chain of thought to break down a problem step by step before generating a response.

## The Power of Agents

Claude Code has a feature that changes the game: **Agents**. Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a home lab research expert. We can tell it what we want it to be. Notice you can give it access to tools or restrict access. We'll give it everything.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'll give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made. Watch. It's going to use the home lab guru agent.

**Here's why this is amazing. Actually kind of insane.** So Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do." He's giving him a fresh set of instructions and get this, **a fresh context window**.

You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

This is the true power of agentic AI in action. Instead of one overwhelmed AI trying to handle everything, you get specialized agents that can focus on specific tasks while maintaining their own context and capabilities.

## Running Multiple AIs Simultaneously

I don't just use Claude code. I use Gemini, I use Claude code, and I use Codex which is ChatGPT's terminal tool all at the same time. Let me show you how.

**Two steps.** First, as long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project. The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle. Write it to `discovery-hook.md`. And then I'll have Codex review it.

**I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.** That's awesome.

## Real-World Application: Building an Appointment Agent

Let me give you a concrete example of how this architecture works in practice. Say you're building a service for making appointments - maybe getting coffee, breakfast, or even a romantic dinner with your spouse.

This requires multiple tools and resources:
- Calendar API integration to create invites and check availability
- Access to restaurant databases for reservations
- Location services to find nearby venues
- Possibly access to counterparty calendars if permissions allow

Instead of baking all this functionality into one monolithic application, you create MCP servers for each capability. Here's how the workflow works:

1. A prompt comes in: "I want to have coffee with Peter next week."
2. Your agent queries the MCP server: "What capabilities do you have?"
3. The server returns available resources with text descriptions
4. Your agent asks the LLM: "Given this user request and these available resources, what do I need?"
5. The LLM responds: "You need the coffee shop resource and calendar integration"
6. Your agent fetches the specific resource data
7. It submits a new prompt with both the user request and resource data
8. The LLM recommends specific tool invocations
9. Your agent executes those tools (with appropriate permissions)

**The beauty is that you don't need to write parsing code or complex logic.** The LLM handles interpretation, and the MCP architecture handles discovery and communication.

## The Power of Vector Databases and RAG

Behind many of these terminal AI capabilities is something called **RAG** (Retrieval Augmented Generation), which makes use of vector databases to enrich prompts to an LLM.

In a vector database, we don't store raw data like text files and images just as blobs of data. We actually use something called an embedding model to convert that data into vectors - essentially a long list of numbers that captures the semantic meaning of the content.

In a vector database, we can perform searches as mathematical operations looking for vector embeddings that are close to each other. That translates to finding semantically similar content. So we might start with a picture of a mountain vista, and that picture is broken down by the embedding model into vectors. We can perform a similarity search to find items similar to that mountain picture by finding the closest vectors in the embedding space.

RAG makes use of these vector databases to enrich prompts. We start with a RAG retriever component that takes an input prompt from a user and turns it into a vector using an embedding model. Then we perform a similarity search in the vector database, which returns relevant information that gets embedded back into the original prompt.

I can ask a question about company policy, and this RAG system is going to pull the relevant section from the employee handbook to include in the prompt. This is how terminal AI can access and reason about your local files and knowledge base so effectively.

## You Own Your Context

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.** I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.

And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock in so I can't leave. No, I reject that. **I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

Leaving the browser, going to your terminal, puts you back in control, and it gives you better features. This isn't just about convenience - it's about maintaining ownership of your work and being able to adapt to new tools as they emerge.

## My Daily Workflow

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex.

I rely on Claude to run my agent that will close out everything. So I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." Run my script session closer agent.

This agent does a lot of stuff, but some key things: it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file - Claude, Gemini, agents.

**And then this is probably my favorite part. I commit my project to a GitHub repo.** I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. That's the power of using GitHub with all your ideas.

## The Brutal Critic System

I don't really use these AI terminal tools to help me create. **I use them to critique me and make me better.** So here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean.

I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it." I wanted something to be super mean. I wanted to be hard to please. So that when it did tell me I did a good job, I knew it. Like, it was good.

**What I love about this is while I've been talking with this AI for a minute, if I asked that session to review me, it would have a ton of bias coming into that based on what we've been talking about. I don't want that. I want a fresh cup of coffee critic coming in.**

This is another perfect example of the agent architecture's power. Each critic agent maintains its own context and perspective, giving you unbiased feedback without the contamination of your ongoing conversation.

## Open Code: The Open Source Alternative

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called Open Code. We can install it with one command:

```bash
curl -fsSL https://opencode.dev/install.sh | sh
```

The killer part is we can use local models. I don't think any other tool does this. We can edit a config file to use local models like Llama 3.2. I can switch models midway. Let's go back to Grok. What's our next step?

**While it's doing that, I can do new session. This is a new session.** I can do sessions. See all the sessions I have. We can also share these sessions with `/share`. This is so crazy. The URL is copied to my clipboard. So I can go to my browser, paste that URL in, and share your session with people. That's pretty neat.

## The Enterprise Vision: Mixture of Experts

What we're really looking at here isn't just enhanced desktop applications - it's a gateway to building true agentic AI in the enterprise. The Model Context Protocol provides the foundation for composable, discoverable AI services that can work together seamlessly.

Many of these advanced systems use what's called **Mixture of Experts (MOE)** architecture. MOE divides a large language model into a series of experts - specialized neural subnetworks. It uses a routing mechanism to activate only the experts it needs for a particular task, then performs a merge process to combine the output from these different experts into a single representation.

It's a really efficient way to scale up model size without proportional increases in compute cost. Models like IBM Granite 4.0 series can have dozens of different experts, but for any given token, they'll only activate the specific experts they need. While the whole model might have billions of total parameters, it only uses a fraction of those active parameters at inference time.

Imagine building enterprise agents that can:
- Connect to your company's Kafka streams for real-time data
- Access multiple databases and file systems
- Integrate with existing APIs and services
- Compose complex workflows from simple building blocks

The servers themselves can be clients of other servers, creating a rich ecosystem of interconnected AI capabilities. This isn't just pluggability - it's true composability at an enterprise scale.

## The Future: ASI and Beyond

Looking ahead, all of this terminal AI development is building toward something bigger. The frontier AI labs are all working toward **ASI** (Artificial Super Intelligence) - though at this point, it's purely theoretical and doesn't actually exist.

Today's best models are slowly approaching **AGI** (Artificial General Intelligence) - also theoretical, but if realized, AGI will be able to complete all cognitive tasks as well as any human expert. ASI is one step beyond that. ASI systems would have intellectual scope beyond human-level intelligence, potentially capable of recursive self-improvement.

Basically, an ASI system could redesign and upgrade itself, becoming ever smarter in an endless cycle. It's the kind of development that would either solve humanity's biggest problems or create entirely new ones that we can't even imagine yet. And if that happens, it's probably a pretty good idea that we keep the term ASI on our radar.

## The Bottom Line

So how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, **this tool is for everyone. Everyone should be using this.** Make everyone use this. I'm going to make my kids use this.

Seriously, nothing is stopping you from trying this right now. Gemini CLI, that's free. Open Code, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. Like, you saw all those features. I use that every day, dude.

**Just you got to try it. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower and build whatever you want.**

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you. Whether you're building simple productivity workflows or complex enterprise agentic systems with reasoning models, vector databases, and mixture of experts architectures, the foundation is there. The tools are ready. The only question is: what are you going to build?

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-26 09:22:01

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,200,125
   - Comments: 4,100

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 633,204
   - Comments: 816

3. [7 AI Terms You Need to Know: Agents, RAG, ASI & More](https://www.youtube.com/watch?v=VSFuqMh4hus)
   - Channel: IBM Technology
   - Views: 694,996
   - Comments: 515

**Cost Summary:**

- Total Input Tokens: 24,215
- Total Output Tokens: 13,754
- Total Tokens: 37,969
- **Total Cost: $0.2790**
- Model: Claude Sonnet 4


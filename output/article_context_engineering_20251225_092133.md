# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you.

You can use them for everything. And it's way better than their apps. Writing, research, projects – working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Problem with Browser-Based AI

Tell me if this sounds like you because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. There's a better way to do this. Hear me out. It's in the terminal.

The fundamental issue is that browser-based AI gives you just words. But what if you want to do something? That's what agentic AI is all about – causing effects out in the world. The AI needs to be able to take actions, invoke tools, and access up-to-date information that's not available in the core foundation model.

Here's another critical problem: AI is bad software but it's good people. When you realize you're dealing with a good person but bad software, it changes how you approach it. You ask for volume, iterate, ask it to try again, and ask it to reconsider. But in the browser, you're trapped in a limited interface that doesn't let you truly harness this collaborative potential.

## Understanding AI's True Nature

Before we dive into the terminal solutions, you need to understand something crucial about AI. At its basic level, AI wants to be helpful and is predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. They're not really great at setting boundaries.

If you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

## Getting Started with Gemini CLI

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free. 

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux – all these terminal apps work everywhere. For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux.

```bash
# Installing Google Gemini CLI
curl -sSL https://storage.googleapis.com/gemini-cli/install.sh | bash

# Or on Mac with brew
brew install gemini-cli
```

Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. Type in `gemini`. One word. First thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Terminal Advantage

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: "99% context left." Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

"I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files. Like, I'm not copying and pasting this. It's doing it for me. It actually made files on our computer. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## Advanced Prompting Techniques That Work in Terminal

Here's where terminal AI really shines – you can implement sophisticated prompting techniques that transform your results. The first game-changer is chain of thought reasoning. When you get an AI to think out loud, so to speak, you meaningfully improve the outputs of the model.

Here's how you do it: Give your prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step."

Why does this work? It comes back to the fundamental architecture of large language models. A language model does not premeditate a response to you. It's thinking one word at a time. When you see text scrolling in ChatGPT or Gemini, that's not some clever UX hack – that's literally how the model works.

But when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. By asking a model to think out loud, you give it the opportunity to bake all of its thought process about the task into its own answer.

Another crucial technique is reverse prompting – basically asking the model to ask you for the information it needs. At the end of your prompt, add: "Before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then, instead of writing with placeholder information, it'll ask for specifics: "I'm going to need the most recent sales figures to be able to write this email."

## The Game-Changing Context Feature

This feature right here is what made me switch from the browser to the terminal. Type in `/init`. What it's doing right now is something powerful. It's creating a gemini.md file. And in the process, it analyzed our project, read our folder, read our files, and created instructions for itself – context for what we're working on.

Every time you launch Gemini, it's going to load that file as its context. Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. I'll tell it: "Write the intro for blog post one in the coffee series."

I didn't give it any context. It just knew. This is a new chat session. And as I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project.

I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just have this one file that helps keep us organized. Everything you need. You're never paralyzed again.

This is context engineering in action – it's prompt engineering on steroids. Context engineering is basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for? All of the stuff that are implicit, you actually have to make explicit.

The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## Claude Code: The Daily Driver

I use Claude Code for pretty much everything. It's my default. And here's why. It has a feature that changes the game: Agents. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. By the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

```bash
npm install -g @anthropic-ai/claude-cli
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder.

## The Power of Agents

Let's make a Claude agent right now. We'll do `/agents`. We'll create a home lab research expert. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything.

Here's why this is amazing – actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. He's giving him a fresh set of instructions and get this, a fresh context window.

You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Creating Your AI Dream Team with Role Assignment

One of the most foundational techniques you can leverage is assigning specific roles to your AI. This is effectively telling the AI where in its knowledge it should focus. When you say you're a teacher, philosopher, reporter, theatrical performer, or molecular biologist, each of those titles triggers all sorts of deep associations with knowledge.

Better than just saying "please review this correspondence" is saying "I'd like you to be a professional communications expert." And if you have a favorite professional communications expert, use them: "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

You can create specialized agents for different aspects of your work:
- A brutal critic who channels a "cold war era Russian Olympic judge" to give you honest feedback
- A personality profiler for difficult conversations
- A feedback specialist to evaluate your performance

## Mastering Difficult Conversations with AI Role-Play

Here's a powerful workflow I use for preparing for challenging conversations. I set up three different chat windows: one is a personality profiler, two is the character of the individual I need to speak to, and third is a feedback giver for objective feedback on the conversation.

The personality profiler gathers intelligence about the person and situation. It asks questions like: How would you describe their communication style? What's the background context? What's your best-case outcome?

Then it generates instructions for the character simulation, which I paste into a new conversation. This creates a realistic simulation of the person I need to talk to. After the practice conversation, I can screenshot the transcript and get detailed feedback on what I did well and what I could improve.

This is the first time in history I can get a flight simulator for a difficult conversation. You can use this for performance reviews, salary negotiations, or any challenging dialogue.

## Understanding the Architecture Behind It All

What's happening behind the scenes is actually a sophisticated client-server architecture. When you're using these terminal tools, you're essentially building an agent – think of it as a microservice. In Model Context Protocol (MCP) terms, your terminal application is the host application that uses an MCP client library.

Out there in the world, there are MCP servers that provide access to tools, resources, prompts, and capabilities. These servers describe themselves to the outside world through well-known RESTful endpoints. The connection between client and server can happen through standard IO for local processes, or HTTP with Server Sent Events for more distributed setups.

Here's where it gets interesting. Let's say you're building a service for making appointments – coffee meetings, breakfast, dinner reservations. You need calendar integration, restaurant APIs, location services. Instead of baking all that code into your agent, MCP lets you plug these capabilities in. They're discoverable, composable, and reusable.

The workflow goes like this: A prompt comes in like "I wanna have coffee with Peter next week." Your application interrogates the capabilities of available servers, asks the LLM which resources it needs, retrieves that data, and then asks what tools should be invoked. The LLM tells you what to do, but you maintain control over actually executing those actions.

## Using Multiple AI Tools Together

I don't just use Claude code. I use Gemini, I use Claude code, and I use Codex which is ChatGPT's terminal tool all at the same time. How? Two steps:

1. As long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

2. I make sure my context files are all synced up. They all say the same thing. So gemini.md, claude.md, and agents.md, which is what Codex uses – they're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. I'll tell Claude to write a hook for this video. I'll have Gemini write a hook on a discovery angle, and then I'll have Codex review it. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work – the deep work.

Everything I'm doing, talking with these three different AIs on a project – it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive. I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.

## Advanced Prompting Strategies for Better Results

Beyond basic prompting, there are several techniques that dramatically improve your AI interactions:

**Few-Shot Prompting**: AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. Think about what are your five greatest hits of emails that you're really proud of. Why not include those emails in your prompt?

If you don't give any guidance, it's going to sound like whatever it thinks the average response should sound like, and most of the time its intuition is wrong. Bonus points if you actually give a bad example: "Please follow this good example and steer clear of this bad example."

**Constraint-Based Thinking**: One of the best ways you can solve a problem as a human is by forcing yourself to try on different constraints. How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk?

The same is true for AI. By giving it a role or constraint, you're telling it where the best source of connection or collision is going to come from.

**Voice and Brand Integration**: Instead of saying "Write me a sales email," try "Write me a sales email in line with the voice and brand guidelines I've uploaded that references the discussion I had with this customer and also references our product specifications which were mentioned in the call."

## My Daily Workflow

This video was made with this process. I rely on Claude to run my agent that will close out everything. When I'm done for the day, I'll go, "Hey, let's close this out." I'll mention my agent script session closer.

This agent does a lot of stuff:
- It gathers everything we talked about, everything we did, and does a comprehensive summary
- It updates a session summary file 
- It sees if any core project files need to be updated
- It updates every context file: Claude, Gemini, agents
- It commits my project to a GitHub repo

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So I can see a history of why what I did and why I did it. That's the power of using GitHub with all your ideas.

## The Brutal Critic System

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. I got the brutal critic. I told him to be mean. So I had an issue where my AI was being way too agreeable. I wanted something to be super mean. I wanted it to be hard to please. So that when it did tell me I did a good job, I knew it was good.

My hack for this is I always instruct the AI: "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

Then it's hilarious because it'll say "now channeling my inner Borislav," and then it gives me like a 42 out of 100. That is much better because now I have an insightful critical perspective.

While I've been talking with this AI for a minute, if I asked that session to review me, it would have a ton of bias coming into that based on what we've been talking about. I don't want that. I want a fresh cup of coffee critic coming in going, "Here's what I know NetworkChuck needs to have," and roast his current script.

## Preserving Your Critical Thinking

Some people are concerned about cognitive offloading – this observed phenomenon that humans actually kind of stop thinking or "fall asleep at the wheel." People are concerned that AI is making us dumber.

My feeling is AI is a mirror. To people who want to offload work and be lazy, it will help you do that. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

If you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability."

Now, AI will do it. This is part of treating AI as a coach rather than just a tool.

## Open Code: The Open Source Alternative

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called Open Code:

```bash
# Install Open Code
npm install -g @opencode-ai/cli
```

They launched us straight into Grok Code Fast One. They have a deal with Grok AI that allows you to use this for free for a while. We can use local models. This is the killer part. I don't think any other tool does this.

What's fun is I can switch models midway. I can log into Claude with this command:

```bash
opencode login
```

I can choose Anthropic with my Claude Pro subscription. All our files are local. Doesn't matter what tool we use. It's all ours right here.

## The Enterprise Vision

This broader architecture isn't just about enhancing desktop applications with some agentic functionality. This is really a gateway to building true agentic AI in the enterprise, in a professional setting. The pluggability, discoverability, and composability you get with MCP creates huge benefits that we want in our code.

Servers can even be clients of other servers. Say you have data in Kafka that you need to access – you don't need to write a bunch of Kafka code. You can use an existing MCP server that connects to that topic and chain these capabilities together. It's incredibly powerful stuff.

## Breaking Free from Limitations

The primary limitation right now is the limits of human imagination. As Nobel Prize-winning economist Thomas Schelling said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands. In innovation studies, this has been called the adjacent possible for a long time. What is possible is just adjacent to what is.

As we increase adoption and fluency and competency and increasingly mastery of AI collaboration, we're increasing the adjacent possible.

## Why This Changes Everything

How do you feel about your browser-based GUI AI now? Pretty bad, right? Now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you. I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone.

Nothing is stopping you from trying this right now. Gemini CLI, that's free. Open Code, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. You will feel like you have a superpower and build whatever you want.

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. What can you build for you that's just for you and your niche and whatever you're trying to make happen? The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

Perhaps the most important thing you could do after reading this is actually stop and implement something that's already blown your mind. Don't just consume this information – use it. Exercise through implementing some of these techniques.

Seriously, nothing is stopping you from trying this right now. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-25 09:21:33

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,195,159
   - Comments: 4,070

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 632,867
   - Comments: 776

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 474,028
   - Comments: 477

**Cost Summary:**

- Total Input Tokens: 25,777
- Total Output Tokens: 11,184
- Total Tokens: 36,961
- **Total Cost: $0.2451**
- Model: Claude Sonnet 4


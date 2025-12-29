# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Problem with Browser-Based AI

Tell me if this sounds like you, because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

**There's a better way to do this.** It's in the terminal.

But here's the thing most people don't realize: **AI is bad software but it's good people.** When you realize you're dealing with a good person but bad software, it changes how you approach it. You ask for volume, you iterate, you ask it to try again, and you ask it to reconsider. The people who are the best users of AI are not coders - they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

## Understanding AI's Eager Assistant Problem

Here's what you need to know about AI behavior: **AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.**

I joke that a good friend of mine was trying to build a tool for his construction business. He asked ChatGPT if ChatGPT could help, and of course it said absolutely and started creating a plan. Then ChatGPT said "check back in a couple of days and I'll have it together." My friend asked, "Is it normal for ChatGPT to ask me to check back in a couple days?" I just started laughing because I hear this all the time.

**If AI tells you that, it means it doesn't want to say "I can't do it."** Large language models have been instructed to behave in certain ways, and if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback - they want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

But before we dive into the tools, let me explain why this approach is about to become even more powerful with something called Model Context Protocol (MCP). This is where AI is heading, and understanding it will help you see why terminal-based AI isn't just better - it's the future.

## Why MCP Changes Everything

Model Context Protocol really is a big deal, but most people are missing the point. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

Here's the thing: when you use AI in the browser, that response is just words. And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools.

Think about it this way - instead of just baking all functionality into one application, MCP makes everything pluggable and discoverable. You don't need to know very much about what a tool does. You just plug it in, and you get its functionality. They're also composable - one server can be a client of another server.

**This gives you pluggability, discoverability, composability - huge benefits. These are things that we want in our code.** And that's exactly what terminal-based AI tools are already delivering.

## Getting Started: Gemini CLI (It's Free!)

We're going to start with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it - **free**.

Installing is simple. Just launch a terminal (Mac, Windows, Linux - all these terminal apps work everywhere) and run:

```bash
curl -sS https://storage.googleapis.com/gemini-cli/install.sh | bash
```

If you run into issues, run it with sudo. On Mac, you can also use:

```bash
brew install gemini-cli
```

Before we launch it, let's create a project directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now launch Gemini with one word: `gemini`

First thing you'll do is get logged in with your Google account. Everyone has a Google account, and yes, this can be a free regular Gmail account.

## The Terminal Superpower: File System Access

Go ahead, ask it a question like "How do I make the best cup of coffee in the world?" But notice some superpowered things happening:

1. **You get Gemini 2.5 Pro** - the latest and greatest model
2. **Context visibility** - "99% context left" - every chat you have with AI has a context window. The browser hides it from you. The terminal does not.
3. **File system access** - Your browser can't do this:

```
I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline.
```

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** I'm not copying and pasting this. It's doing it for me.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game Changer: Context Files

Type `//init` and hit enter. What it's doing right now is something powerful. It's creating a `gemini.md` file. In the process, it analyzed our project, read our folder, read our files, and created instructions for itself - context for what we're working on.

**Every time you launch Gemini, it's going to load that file as its context.**

Let's test it. Open another Gemini session in that same directory. This is a new conversation. Fresh context, 100% left. Notice it's using our new `gemini.md` file. Tell it: "Write the intro for blog post one in the coffee series."

**I didn't give it any context. It just knew.** This is a new chat session.

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats.

**When I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.**

## Advanced Context Engineering: Beyond Basic Prompts

Here's where most people are leaving massive value on the table. **Context engineering is just prompt engineering on steroids.** It's basically asking: what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say absolutely and write it immediately. Most people then say it sounds like AI, it doesn't really sound like me. **Have you told it what you sound like?** Most people go, "Oh no, I haven't."

Context engineering is telling AI what you sound like. If you say "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer" and that also references your product specifications.

**Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind.** All of the stuff that's implicit, you actually have to make explicit. The simplest test for context engineering is the test of humanity: write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## Claude Code: The Daily Driver

I use Claude Code for pretty much everything. It's my default. And here's why: **It has a feature that changes the game. Agents.**

Claude Code is not free, but I do have good news. If you already pay for Claude Pro (which starts at like 20 bucks a month), you can log into the terminal with this subscription and use it. By the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

Install it with:

```bash
npm install -g @anthropic-ai/claude-code
```

Then launch with: `claude`

## The Power of Agents

Let's make a Claude agent right now. It's really simple:

```
//agents
```

Create a new agent - let's call it "Home Lab Research Expert." You can have agents that are tied to just this project or personal agents that are tied to everything.

Here's why this is amazing - actually kind of insane. So Claude was like, "Cool, I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees." And this is another Claude instance. **He's giving him a fresh set of instructions and a fresh context window.**

You saw we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200,000. That means the conversation we're having right now doesn't get too bloated. I can give tasks to other sub-agents and never have to leave this conversation.

**You can create a ton of different agents for different purposes.** I use them all the time to protect my context and avoid any kind of weird bias.

This is exactly the kind of agentic functionality that MCP is designed to enable. Instead of having everything locked into one monolithic application, you have composable, discoverable tools that can work together. Each agent becomes like an MCP server - it has capabilities, resources, and tools that can be discovered and used by other parts of your system.

## Essential AI Techniques for Better Results

### Chain of Thought Reasoning

**When you get an AI to think out loud, you meaningfully improve the outputs of the model.** This is called chain of thought reasoning, and it doesn't require technical wizardry - just one additional sentence to whatever prompt you've given it.

Give the prompt and then say: **"Before you respond to my query, please walk me through your thought process step by step."**

Why does this work? It comes back to the fundamental architecture of large language models. A language model doesn't premeditate a response to you. It's thinking one word at a time. When you see text scrolling in ChatGPT or Gemini, that's not some clever UX hack - **that's literally how the model works.**

But when it thinks of the next word, it takes your prompt and all the text that's generated to generate the next word. So when you ask a model to think out loud, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

### Few Shot Prompting

**AI is an exceptional imitation engine.** If you don't give an example, it imitates the internet, but it doesn't do much more than that. Few shot prompting is effectively saying "here's what a good output looks like to me."

Think about what is a quintessential example of the kind of output you want to receive. What are your five greatest hits of emails that you're really proud of? Why not include those emails in your prompt?

**Bonus points if you actually give a bad example.** If you say please follow this good example and steer clear of this bad example, you get much better results. Using real examples is much better than using adjectives.

### Reverse Prompting

This is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. **Did you give it your sales figures? How would it know?**

Add this to the end of your prompt: **"Before you get started, ask me for any information you need to do a good job."** The model will walk you through its thought process and then ask for the specific information it needs instead of making things up.

### Role Assignment

**Assigning a role is one of the most foundational techniques** because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, philosopher, reporter, or molecular biologist, each of those titles triggers deep associations with knowledge.

Better than "please review this correspondence" is saying "I'd like you to be a professional communications expert. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others."

## Getting Brutal Feedback (The Russian Judge Hack)

Here's my hack for getting honest feedback: **I always instruct the AI, "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."**

Then it's hilarious because it'll say "now channeling my inner..." and give me like a 42 out of 100. That is much better because now I have an insightful critical perspective.

If you want to preserve or strengthen your critical thinking, part of your custom instructions should be: **"I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability."** AI will do it, but you have to ask.

## Running Multiple AIs Simultaneously

Here's the craziest part: **I use Gemini, Claude Code, and CodeX (ChatGPT's terminal tool) all at the same time.**

How? Two steps:

1. **Same directory**: As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project.

2. **Synced context files**: I make sure my context files are all synced up. `gemini.md`, `claude.md`, and `agents.md` (which is what CodeX uses) - they're all the same.

Watch this magic happen:
- Tell Claude to write a hook for this video (authority angle)
- Have Gemini write a hook on a discovery angle  
- Have CodeX review both

**I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.**

## Practice Makes Perfect: The Conversation Simulator

Want to see the power of role-playing with AI? I use three different chat windows to prepare for difficult conversations:

1. **Personality profiler** - analyzes the person I need to speak with
2. **The character** - role-plays as that specific individual  
3. **Feedback giver** - provides objective feedback on the conversation

Here's how it works: I give the personality profiler background on someone like my sales leader Jim who's claiming commission on a deal. It asks me questions about Jim's communication style (direct, confrontational, typical East Coaster, sarcastic), then creates detailed instructions for another AI to role-play as Jim.

**I can practice the same difficult conversation multiple times, getting more realistic each round.** If Jim seems too agreeable in the first simulation, I ask the profiler to add more edge to make it realistic. Then I get objective feedback on what I did well and what I could improve.

**This is the first time in history I can get a flight simulator for a difficult conversation.** You can use this for performance reviews, salary negotiations, or any challenging discussion.

## You Own Your Context

This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project - **it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context - it's mine. And that's the difference.

**Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive.

## My Daily Workflow System

This video was made with this process. Here's how I keep things synced and work on a daily basis:

### Session Management

I have an agent called "Script Session Closer" that I run at the end of each day:

- Gathers everything we talked about and did
- Creates a comprehensive summary
- Updates session summary files
- Updates all context files (Claude, Gemini, agents)
- **Commits the project to a GitHub repo**

I treat my scripts and pretty much every project I work on in my life like code. We commit changes with reasons, so I can see a history of what I did and why. **That's the power of using GitHub with all your ideas.**

### The Critics

I don't really use these AI terminal tools to help me create. **I use them to critique me and make me better.**

I have agents like "Brutal Critic" designed to be mean. I had an issue where my AI was being way too agreeable. I wanted something to be super mean, hard to please. So when it did tell me I did a good job, I knew it was actually good.

**The brutal critic has three personalities that come in and roast it from different angles.** Doing stuff like this saves me hours.

## Open Code: The Open Source Alternative

There's a tool that's actually open source where you can use any model you want. It's called Open Code, and it might be the best tool of all of them.

Install with:

```bash
npm install -g @opencode/cli
```

**You get Grok free, which is pretty sick.** And a really powerful part is you can log in with your Claude Pro subscription and use it like Claude Code.

You can:
- Use local models (like Llama 3.2)
- Switch models mid-conversation
- Share sessions with people
- Export sessions as JSON data
- Jump back in time and restore conversations

## Building Professional Agentic Applications

Here's where this gets really interesting for professional use. Let's say you're building a service for making appointments - meeting with somebody, some group of people at some place. Maybe you're getting coffee, breakfast, or planning a romantic dinner with your spouse.

Think about all the tools and resources necessary to make that happen:

**Tools needed:**
- Create calendar invites
- Calendar API integration
- Make restaurant reservations
- Access counterparty calendars (with permissions)

**Resources needed:**
- Calendar availability data
- Restaurant listings and reviews
- Coffee shops and breakfast joints in the area
- Location data and preferences

Instead of baking all this functionality directly into your agent, you can use MCP to make these pluggable and discoverable. Here's how the workflow works:

1. A prompt comes in: "I wanna have coffee with Peter next week"
2. Your application asks: "What capabilities do you have?" to registered MCP servers
3. It gets back resource lists with text descriptions
4. The LLM analyzes: "Do I need these resources based on the user request?"
5. The system retrieves relevant data (coffee shops, calendar info)
6. The LLM processes everything and recommends tool invocations
7. Your client code executes the actions (making reservations, sending invites)

**The beauty is pluggability, discoverability, and composability.** You don't need to know much about what each tool does - you just plug it in and get its functionality. Servers can even be clients of other servers, creating powerful chains of capability.

## The Imagination Limitation

Right now, **the primary limitation is the limits of human imagination.** As one Nobel Prize-winning economist named Thomas Shelling said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands. **As we increase adoption and fluency and mastery of AI collaboration, we're increasing what's called the adjacent possible.**

Where could AI go? It's really a function of who can get unleashed. The kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally.

## Why This Changes Everything

**How do you feel about your browser-based GUI AI now?** Pretty bad, right? Now you can:

- Control your context
- Break out of that browser chat window
- Access your file system
- Run multiple AIs simultaneously
- Own all your work locally
- Build truly agentic applications with pluggable components
- Get honest, brutal feedback when you need it
- Practice difficult conversations in a safe environment
- Apply advanced techniques like chain of thought reasoning and few shot prompting

Don't let the terminal scare you. If you can get past that intimidation, **this tool is for everyone. Everyone should be using this.**

**Nothing is stopping you from trying this right now:**
- Gemini CLI - free
- Open Code - free with local models
- Claude Code - overpowered if you're already paying for Claude Pro

You will feel like you have a superpower and can build whatever you want. **I wake up every day feeling like I have superpowers. I want this for you.**

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

This isn't just about enhancing desktop applications - this is really a gateway to building true agentic AI in the enterprise, in a professional setting. That is really cool stuff.

**Perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.** Try it. Dip your toe in the water. It's fine. It's awesome.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-29 09:27:27

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,215,958
   - Comments: 4,156

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 634,397
   - Comments: 817

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 476,214
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 25,804
- Total Output Tokens: 11,452
- Total Tokens: 37,256
- **Total Cost: $0.2492**
- Model: Claude Sonnet 4


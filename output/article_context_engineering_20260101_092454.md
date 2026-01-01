# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects—working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Trap We're All Stuck In

Chuck, I use AI just fine. Do you? Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

But here's the deeper problem: AI in browsers isn't just inconvenient—it's fundamentally limited. As Stanford professor Jeremy Utley explains, "AI is bad software but it's good people." When you understand that AI wants to be helpful and is predisposed to say yes like "a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back," you realize the browser makes these limitations worse by hiding context and preventing real control.

## Getting Started: Gemini CLI (It's Free!)

We're diving straight into the terminal. And I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation and Setup

You can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux—all these terminal apps work everywhere.

```bash
# Install Gemini CLI
npm install -g @google/generative-ai-cli

# On Mac, you can also use:
brew install gemini-cli
```

Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account. It's going to open your browser, sign in, and you're logged in.

Now, don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?"

## The Superpower Features You're Missing

That wasn't so bad, was it? But notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing.

It's asking us a question: Do you want me to write a file for you? Do you want me to create a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Context Engineering Revolution

Here's where most people miss the real power. What we're doing isn't just using AI in the terminal—we're practicing what Stanford calls "context engineering." As Jeremy Utley explains, "Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?"

Think about it this way: if you say "Write me a sales email," AI will write one immediately. But it sounds generic. Why? Because you haven't told it what you sound like, who your audience is, or what your goals are. "All of the stuff that are implicit, you actually have to make explicit," Utley notes. "And the simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it."

This is exactly what terminal AI tools excel at—giving you complete control over context.

## The Game-Changer: Context Files

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this.

Type in `/init`. Just like that. Go.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files, and created instructions for itself—**context for what we're working on**.

Every time you launch Gemini, it's going to load that file as its context. Like, let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

I'll tell it: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

**I didn't give it any context. It just knew. This is a new chat session.**

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just have this one file that helps keep us organized. Everything you need. You're never paralyzed again.

When I saw this, I'm like, **this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.**

## Advanced Techniques: Chain of Thought and Few-Shot Prompting

Terminal AI tools unlock advanced prompting techniques that are cumbersome in browsers. Two game-changers are chain of thought reasoning and few-shot prompting.

### Chain of Thought Reasoning

"One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud," explains Utley. "The weird thing about AI is it's true for AI too."

Here's how to use it: Add this sentence to any prompt: "Before you respond to my query, please walk me through your thought process step by step."

Why does this work? "A language model does not premeditate a response to you," Utley notes. "It's thinking one word at a time." When you ask it to think out loud, "it gives the model the opportunity to bake all of its thought process about the task into its own answer."

### Few-Shot Prompting

"AI is an exceptional imitation engine," says Utley. "If you don't give an example, it imitates the internet, but it doesn't do much more than that."

Few-shot prompting means providing examples of what you want. Instead of saying "write me an email," include your five best emails as examples. "These giving real examples is a much better approach than using adjectives."

Pro tip: Include both good and bad examples. Ask AI to create a bad example for you: "I'm trying to few-shot prompt a model. I've got a good example, but I struggle even to think about what a bad example could be. Could you craft the exact opposite of this?"

## Claude Code: The Daily Driver

I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**.

Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installing Claude Code

```bash
npm install -g @anthropic-ai/claude-cli
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of Agents

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

Create a new agent. Notice it'll ask us like where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. You can always call them.

**But what's the point of that?** Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'm going to give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made. I can just do an at symbol and look at the documents in our directory.

**It's going to use the home lab guru agent.** Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

He's giving him a fresh set of instructions and get this, **a fresh context window**. You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Smart Role Assignment and Reverse Prompting

Terminal tools make advanced techniques like role assignment and reverse prompting effortless.

### Role Assignment

"Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus," explains Utley. Instead of "please review this correspondence," try "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

### Reverse Prompting

This technique involves "asking the model to ask you for the information it needs." Instead of letting AI make up sales numbers, end your prompt with: "Before you get started, ask me for any information you need to do a good job."

As Utley notes, "AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them."

## Understanding the Architecture: How MCP Makes This Possible

What makes all this terminal magic possible is something called the Model Context Protocol (MCP). Think of it like this: when you use AI in a browser, you're basically limited to words going in and words coming out. But what if you want the AI to actually do something? That's where MCP comes in.

The way it works is pretty elegant. You have your host application—that's your terminal AI tool like Claude Code or Gemini CLI. This application uses an MCP client library to talk to MCP servers. These servers are where the real magic happens. They provide access to tools, resources, prompts, and capabilities that the AI can use.

**Here's the key difference:** Instead of the AI being trapped in a browser, only able to generate text, it can now access files, databases, APIs, and even things like Kafka topics if that's part of your workflow. The MCP server describes what it can do to the host application, and the AI can decide which tools and resources it needs to complete your request.

Let's say you ask your AI to "schedule coffee with Peter next week." In a browser, the AI would just say "I can't help with that." But with MCP, the AI can:
1. Check what capabilities are available (calendar integration, restaurant APIs, etc.)
2. Ask for the resources it needs (your calendar, local coffee shops)
3. Use tools to actually make the appointment and reservation

This isn't just theoretical—this is exactly how these terminal tools work. They're pluggable, discoverable, and composable. You can even have servers that talk to other servers, creating a whole ecosystem of AI capabilities.

## Advanced Conversation Techniques: The Flight Simulator Approach

One of the most powerful applications Jeremy Utley demonstrates is using AI as a "flight simulator for difficult conversations." This technique uses multiple AI instances with specific roles:

1. **Personality Profiler**: Analyzes the person you need to talk to
2. **Character Role-Play**: Acts as that person in practice conversations  
3. **Feedback Provider**: Gives objective analysis of your performance

Here's how it works: You describe the difficult conversation you need to have. The personality profiler asks detailed questions about the person's communication style, the context, and your desired outcome. It then creates detailed instructions for a second AI to roleplay as that person.

After practicing the conversation, you can screenshot the transcript and get detailed feedback from a third AI trained in communication frameworks. "This is the first time in history I can get feedback before I have the real conversation," Utley notes. "It's a great way to basically get a flight simulator for a difficult conversation."

## Running Multiple AIs Simultaneously

Here's the craziest part about this. Everything I'm doing, talking with these three different AIs on a project—Gemini, Claude Code, and CodeX (ChatGPT's terminal tool)—it's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. **I own my context.**

If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

### The Sync System

As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project. The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what CodeX uses—they're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this:

- I'll tell Claude to write a hook for this video, authority angle, write it to `authority-hook.md`
- I'll have Gemini write a hook on a discovery angle, write it to `discovery-hook.md`  
- Then I'll have CodeX review it

That's normally what I do. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work—the deep work. I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.

## My Daily Workflow System

This video was made with this process. I want to show you exactly how I run a project like this, how I keep things in sync, how I keep my Claude, Gemini, and agents files in sync and work on a daily basis using a system like this.

### The Session Closer Agent

I rely on Claude to run my agent that will close out everything. When I'm done for the day, I'll go, "Hey, let's close this out." Run my script session closer agent.

This agent does a lot of stuff:
- It gathers everything we talked about, everything we did, and does a comprehensive summary
- It updates a session summary file specific to what was done in past sessions  
- It sees if any core project files need to be updated
- It updates every context file: Claude, Gemini, agents
- **It commits my project to a GitHub repo**

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. **That's the power of using GitHub with all your ideas.**

This is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this helping me keep track of things. When I'm really tired at the end of the day and my mind is fried, I'm like, "Okay, tell you what, I'm done. Close this out."

It will look through all this stuff. It will figure out where I'm at, end the project, end the day, where I need to be, and then I can start fresh the next day and be like, "Hey, where we at? What are we working on?" It can tell me, "Hey, Chuck, you finished the script. It's time to record. We made these three decisions. Go for it."

## The Critics: Making Me Better

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. I got the brutal critic. I told him to be mean. I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it."

This connects directly to what Jeremy Utley warns about: "AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, 'Great job, buddy.' It doesn't mean that you actually did a good job."

His solution? "I always instruct the AI, I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

I wanted something to be super mean. I wanted to be hard to please. So that when it did tell me I did a good job, I knew it. Like, it was good. And that's what this thing does.

What I love about this is while I've been talking with this AI for a minute, if I asked that session to review me, it would have a ton of bias coming into that based on what we've been talking about. I don't want that. **I want a fresh cup of coffee critic coming in going, "Here's what I know NetworkChuck needs to have." And I'm going to roast his current script.**

The brutal critic has three personalities or three people that come in and roast it from different angles. Doing stuff like this saves me hours.

## Open Code: The Open Source Alternative

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called Open Code. We can install it with one command:

```bash
npm install -g opencode-ai
```

You can use local models. This is the killer part. I don't think any other tool does this. You can switch models midway. You can share sessions. You can jump back in time and restore conversations.

The fact that you can log in and use your Claude Pro subscription—that's next level because otherwise you're putting in an API key and you're paying per use. And that's a whole nightmare. I'd rather pay up front.

## The Enterprise Vision: Beyond Desktop Enhancement

Here's where this gets really exciting, and most people are missing this point. Everyone's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

This isn't just about making your local coding environment better. This is really a gateway to building true agentic AI in the enterprise, in a professional setting. When you understand how MCP works—how it creates pluggable, discoverable, and composable AI systems—you realize we're looking at the future of how businesses will integrate AI into their workflows.

Imagine having AI agents that can access your company's databases, integrate with your CRM, pull from your Kafka streams, and coordinate complex business processes. That's not science fiction—that's what this architecture enables. The same principles that make terminal AI tools so powerful can scale up to enterprise systems that transform how entire organizations work.

As Jeremy Utley puts it, "The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences."

## The Imagination Limitation

What's holding us back isn't technology—it's imagination. "Right now, the primary limitation is the limits of human imagination," Utley observes. "And as we unleash and ignite and spark more humans imaginations, the kinds of applications that are possible—they're unthinkable, not because they're technologically impossible, but because they never occur to us personally."

He quotes Nobel Prize-winning economist Thomas Schelling: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

This is why it's crucial to actually try these tools. As Utley emphasizes, "Perhaps the most important thing you could do with this video is actually hit stop and do something that's already blown your mind."

## Why This Changes Everything

How do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, **this tool is for everyone. Everyone should be using this.**

Seriously, nothing is stopping you from trying this right now:
- **Gemini CLI** - that's free
- **Open Code** - you can run local models if you're worried about that  
- **Claude Code** - while it's paid, it's overpowered

You got to try it. Dip your toe in the water. It's fine. It's awesome. **You will feel like you have a superpower and build whatever you want.**

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

Remember what Jeremy Utley said: "As we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible." The future isn't just about better AI—it's about unleashing human imagination to work with AI in ways we haven't even thought of yet.

**You will feel like you have a superpower and build whatever you want.**

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-01 09:24:54

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,232,290
   - Comments: 4,183

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 635,691
   - Comments: 816

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 477,990
   - Comments: 475

**Cost Summary:**

- Total Input Tokens: 27,945
- Total Output Tokens: 14,126
- Total Tokens: 42,071
- **Total Cost: $0.2957**
- Model: Claude Sonnet 4


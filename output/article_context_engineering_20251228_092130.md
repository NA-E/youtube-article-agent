# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects—working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Struggle Is Real

I know what you're thinking: "Chuck, I use AI just fine." Do you? Tell me if this sounds like you because this is how I used to use AI.

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

## Understanding AI's True Nature: It's Good People, Bad Software

Before we dive into the terminal tools, let's understand something crucial about AI. **AI is bad software but it's good people.** A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said check back in a couple of days and I'll have it together. And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

**Large language model has been instructed in certain ways to behave in certain ways. But you have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes.** It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

When you use AI in a browser, you have a prompt and you send that into an LLM. Out of that LLM, you get a response. But there are two fundamental problems here.

That response is just words. And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools. It also needs more up-to-date information or maybe just broader information than what's available in that core foundation model.

The browser locks you into this limited interaction model. **But the terminal breaks you free.**

## Getting Started: Gemini CLI (It's Free!)

We're diving straight into the terminal, and I want you to try it so you can know it's not really scary. The terminal is a fun place. And we're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

Installing is simple. Go ahead and launch a terminal—it doesn't really matter where you launch it. Mac, Windows, Linux, all these terminal apps work everywhere. For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux.

```bash
# Install Gemini CLI
npm install -g @google-ai/generativelanguage-cli

# Or on Mac with brew
brew install gemini-cli
```

If you run into a scary issue, run it with `sudo`. Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" That wasn't so bad, was it? But notice some superpowered things:

- **Gemini 2.5 Pro**: The latest and greatest model
- **99% context left**: Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.
- **File system access**: Your browser can't do this

## The Game-Changing Feature: File System Access

Watch this magic happen. I'll give it this prompt:

"I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources, and then compile the results into a document named `best-coffee-method.md` and then create me a blog plan—just an outline. I'll do the writing."

It's asking us: Do you want me to write a file for you? **Yeah, dude. Go for it.**

This thing can do everything a browser can do, but it has a superpower. **It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. Look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## Context Engineering: The Foundation of AI Mastery

Context engineering—I first heard about it when Andre Karpathy tweeted about it. I think probably Toby Lutke, the CEO of Shopify, also referenced it as well. **Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?**

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, you know, and they'll write it immediately. Well, what a lot of people do is they say, you know, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

**Context engineering, one way to think about it is it's telling AI what you sound like.** If you say, "Write me a sales email," it will. If you say, "Write me a sales email," in line with the voice and brand guidelines I've uploaded, it will write a totally different sales email.

**Your goal is to have an output is as reliable per your specification as possible. But AI can't read your mind.** All of the stuff that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### Never Lose Track Again with Context Files

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, **context for what we're working on**.

Let's take a look at it:

```bash
cat gemini.md
```

While we didn't do much in this project, it knows what's going on. And every time you launch Gemini, it's going to load that file as its context.

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file. And I'll tell it this:

"Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about. **I didn't give it any context. It just knew. This is a new chat session.**

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. **No reexplaining the context, no starting over, no more 20 scattered chats.** We just have this one file that helps keep us organized. Everything you need. You're never paralyzed again.

## Claude Code: The Daily Driver

Now, I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**.

Look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So yeah, you don't have to use API keys. And by the way, **if you can only pay for one AI subscription, Claude Pro is the one I would choose**.

### Installing Claude Code

Let's get it installed with one command:

```bash
npm install -g @anthropic-ai/claude-cli
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of Agents

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a "home lab research expert."

Create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. We'll do just this project.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'm going to give it this prompt and I'm calling it "home lab agent." It'll figure it out. Watch. It's going to use the home lab guru agent.

**Here's why this is amazing. Actually kind of insane.** So Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

He's giving him a fresh set of instructions and get this, **a fresh context window**. You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub-agents and never have to leave this conversation.

## Advanced Techniques: Chain of Thought Reasoning

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. **The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning.**

So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: **"Before you respond to my query, please walk me through your thought process step by step."** That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. **A language model does not premeditate a response to you.**

When you look at ChatGPT or Gemini or many others and you see kind of the text scrolling, that's not some like clever UX hack. That's not some cutesy design decision. **That's literally how the model works. It's thinking one word at a time.**

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. By asking a model to think out loud, you give the model the opportunity to bake all of its thought process about the task into its own answer.

## Few-Shot Prompting: Teaching by Example

Few shot prompting is another very important technique. **You could say it's a predecessor to this kind of modern obsession with context engineering. The idea with few shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that.**

The notion of few shot prompting is effectively saying here's what a good output looks like to me. For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality or whatever it is? Why not include those emails in my prompt for an email?

**These giving real examples is a much better approach than using adjectives.** And bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example.

## The Architecture Behind the Magic: Understanding MCP

What makes all this possible is something called the Model Context Protocol (MCP). This really is a big deal, but most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

Here's how it works architecturally. What we're doing is building an agent—you could think of it as a microservice. There's nothing particularly exotic about this. But in MCP terms, this is called the host application. And the host application uses the MCP client library to create an instance of a client.

Out here, we create an MCP server. This may be a server that already exists that somebody else has built that we want to take advantage of to bring agentic functionality into our service, or this could be a server that we ourselves are creating. Inside the server, we have access to tools, resources, prompts, capabilities that the server makes available and even describes to the outside world.

The connection between client and server can be standard IO for local processes, or HTTP with Server Sent Events for distributed systems. The messages being exchanged are in JSON RPC format.

With MCP's pluggable architecture, you get:
- **Pluggability**: Don't need to know much about what tools do—just plug them in
- **Discoverability**: Servers describe their capabilities automatically
- **Composability**: Servers can be clients of other servers, creating powerful chains

## Advanced Prompting Techniques

### Reverse Prompting: Let AI Ask the Questions

**The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.**

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know?

But if you reverse prompt the model and say at the end of your prompt, "help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this skew in Q2 last year?"

**You basically give the model permission to ask you questions. This is part of the core actually of the teammate not technology paradigm.**

### Role Assignment: Focus AI's Knowledge

**Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus.** So very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just "please review this correspondence" is saying "I'd like you to be a professional communications expert. And if you have a favorite professional communications expert use them. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

## Running Multiple AIs Simultaneously

Gemini, Claude Code, ChatGPT's CodeX. I'm using all three right now to work on this video script. How? Two steps:

1. **Same directory**: As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project.

2. **Synced context files**: I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md` (which is what CodeX uses)—they're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this:

- I'll tell Claude to write a hook for this video (authority angle), write it to `authority-hook.md`
- I'll have Gemini write a hook on a discovery angle, write it to `discovery-hook.md`
- Then I'll have CodeX review it

That's normally what I do. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work—the deep work. They're all using the same context, different roles. **I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work.**

## The Brutal Truth: AI Critics and Feedback

**I don't really use these AI terminal tools to help me create. I use them to critique me and make me better.** I got the brutal critic. I told him to be mean. I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh Chuck, best thing you ever wrote." I'm like, "You're gaslighting me. Stop it."

**AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.**

My kind of hack for this is I always instruct the AI: **"I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."**

And then it's of course hilarious because it'll say now channeling my inner bullshik, you know, it'll say something silly and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

**If you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability.**

## Practice with Difficult Conversations

Here's a practical example of how to use AI for skill development. I typically think about kind of three different chat windows for preparing for difficult conversations:

1. **Personality profiler** - Analyzes the person you need to talk to
2. **The character** - Role-plays as that individual 
3. **Feedback giver** - Provides objective feedback on the conversation

Let's say I need to have a conversation with my sales leader Jim about commission attribution. I'll upload details to the personality profiler, which asks questions like "How would I describe Jim's communication style?" After gathering intelligence, it creates instructions for a role-playing session.

Then I open a new conversation where AI becomes Jim, and I practice the difficult conversation. After the role-play, I can get feedback on my performance - what I did well, what I could improve, and specific talking points to remember.

**This is the first time in history I can get feedback before having the real conversation.** You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback. It's a great way to basically get a flight simulator for a difficult conversation.

## Real-World Example: Building an Appointment Agent

Let's walk through a practical example of how MCP enables powerful agentic applications. Say we're building a service for making appointments—generalized meetings with somebody, some group of people at some place. Maybe we're getting coffee, breakfast, or planning a romantic dinner.

This requires several tools and resources:
- Calendar API integration to create invites and check availability
- Restaurant reservation systems
- Location-based services for finding coffee shops and restaurants
- Access to multiple calendars for scheduling coordination

Instead of baking all this functionality directly into our agent, we can create MCP servers that provide these capabilities. Here's how the workflow works:

A prompt comes in: "I want to have coffee with Peter next week." The host application interrogates the MCP server's capabilities, discovers available resources like "list of coffee shops in the area," and asks the LLM: "Here is what my user said. Here is a list of resources. Do I need these?"

The LLM responds: "Yes, you need resource two—that list of coffee shops looks super interesting." The client fetches that resource data and provides it in the next prompt: "Here is my user prompt. And now here is the resource data. What should I do as a result?"

For tools, the foundation model APIs can actually accept tool descriptions as structured data. The LLM will respond with specific tool invocations: "Yes, invoke this tool, pass these parameters." Your client code then makes the decision to call that tool and cause the effect out in the world.

## The Real Superpower: You Own Your Context

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project—it's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, **it's mine**. And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. **I own my context.**

If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. **I will use all AI. I will use the best AI. No one can stop me.**

## My Daily Workflow System

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is CodeX.

I rely on Claude to run my agent that will close out everything. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent "script session closer."

This agent does a lot of stuff, but some key things:

- Gathers everything we talked about, everything we did, and does a comprehensive summary
- Updates a session summary file specific to updating what are some things that were done in past sessions
- Sees if any core project files need to be updated
- Updates every context file: Claude, Gemini, agents
- **Commits my project to a GitHub repo**

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. **That's the power of using GitHub with all your ideas.**

This is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things. When I'm really tired at the end of the day and my mind is fried, I'm like, "Okay, tell you what, I'm done. Close this out."

It will look through all this stuff. It will figure out where I'm at, end the project, end the day, and then I can start fresh the next day and be like, "Hey, where we at? What are we working on?" It can tell me, "Hey Chuck, you finished the script. It's time to record. We made these three decisions. Go for it."

## Open Source Alternative: OpenCode

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called OpenCode:

```bash
npm install -g opencode-cli
```

The killer part is we can use local models. I don't think any other tool does this. You can switch models midway through a conversation. You can share sessions with people. You can jump back in time and restore conversations.

## The Coaching Mindset: The Key to AI Success

**The people who are the best users of AI are not coders, they're coaches.** They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

**If you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.**

If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. Right? Any good manager, imagine a manager who says, "Don't ask me any questions." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us human with questions unless we give it permission to ask them.

## Why This Changes Everything

So how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can **control your context. Break out of that browser, that chat window**.

This isn't just about enhancing desktop applications with some agentic functionality. This is really a gateway to building true agentic AI in the enterprise, in a professional setting. With MCP providing the architectural foundation, we're looking at a future where AI agents can seamlessly integrate with existing enterprise systems, databases, and workflows.

**Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans imaginations, the kinds of applications that are possible or they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.**

Don't let the terminal scare you. I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, **this tool is for everyone. Everyone should be using this.**

Nothing is stopping you from trying this right now:

- **Gemini CLI**: Free
- **OpenCode**: You can run local models if you're worried about that
- **Claude Code**: Paid, but overpowered

You will feel like you have a superpower and build whatever you want. The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. **I want this for you.**

**Perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.** The adjacent possible expands as more people gain fluency with these tools. Your imagination, combined with AI's capabilities, is the only limit to what's possible.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-28 09:21:30

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,210,511
   - Comments: 4,143

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 633,988
   - Comments: 817

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 475,657
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 27,935
- Total Output Tokens: 14,938
- Total Tokens: 42,873
- **Total Cost: $0.3079**
- Model: Claude Sonnet 4


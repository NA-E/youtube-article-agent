# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm about to show you why. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

The key is understanding that **AI is bad software but it's good people**. When you realize you're dealing with a good person but bad software, it changes how you approach it. You ask for volume, you iterate, you ask it to try again and reconsider. **The people who are the best users of AI are not coders, they're coaches.**

## The Problem with Browser-Based AI

Tell me if this sounds like you because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind.

You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works. At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

But here's what's really happening behind the scenes: **Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right?** You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? **Context windows.**

### Understanding Context Windows: Why AI Gets Dumb

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or DeepSeek, they're kind of like us in that they have memories - short-term memory, which means they can remember things. But also, sometimes they can forget stuff.

Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said. But you're pretty fun to talk to. So we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. Thankfully, you forgot that dumb thing I said. And sometimes we forget the entire point of the conversation.

**ChatGPT does the same thing.** The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. **That limit is its context window.**

Tokens are how an AI counts the words you say to it. A sentence might be 133 characters or 26 words, but an LLM just cares about tokens. That same sentence would actually be 38 tokens. And when you hit that context window limit, **AI starts to hallucinate, forget what you're talking about, and become stinking slow.**

**There's a better way to do this. Hear me out. It's in the terminal.**

## Getting Started with Gemini CLI

We're diving straight into the terminal, and I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux - all these terminal apps work everywhere.

For Mac users:
```bash
brew install gemini-cli
```

For other systems:
```bash
# Standard installation command
```

If you run into a scary issue, run it with sudo just like this. And if you're on Mac, you can also use brew.

### Setting Up Your First Project

Before we launch it, we're going to make a new directory:
```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Terminal Superpower: File System Access

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

**With Gemini 2.5 from Google rocking 1 million tokens, you can tell it your whole life story and it's going to remember it.** And what's crazy is they're saying that 2 million is right around the corner.

But here's where it gets crazy. Your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

This thing can do everything a browser can do, but it has a superpower. **It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files, and created instructions for itself - **context for what we're working on**.

Every time you launch Gemini, it's going to load that file as its context. Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

I'll tell it: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about. I didn't give it any context. It just knew. This is a new chat session.

## Why This Changes Everything

When I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. **Mine, my precious.**

I'm literally using the `gemini.md` file right now for this project. Let me show you a big example. This is the `gemini.md` file for this video. It tracks everything. It describes how I create, project status, major decisions I made, even other documents it should look at.

I'll launch a whole new Gemini session in this project and ask where we're at in the project. Are you seeing this? This has completely changed the way I create or do anything now.

## Claude Code: The Daily Driver

I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, **Claude Pro is the one I would choose**.

### Installing Claude Code

Let's get it installed with one command:
```bash
npm install -g @anthropic-ai/claude-cli
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of Agents

Now, I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**.

Look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a home lab research expert.

You can give it access to tools or restrict access. We'll give it everything. Choose our model. Sonnet's great. There's our agent. Press enter to save.

But what's the point of that? You're right. But watch this. I'm going to give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made.

Watch. It's going to use the home lab guru agent. Now, here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers."

**This is another Claude instance.** He's giving him a fresh set of instructions and get this, **a fresh context window**. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Advanced Prompting Techniques That Make Terminal AI Unstoppable

Here's where terminal AI becomes truly powerful - when you combine it with advanced prompting techniques that most people never learn. These aren't just tricks; they're fundamental ways to communicate with AI that transform your results.

### Context Engineering: The Foundation

Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, it sounds like AI. It doesn't really sound like me. And what I often say is, **have you told it what you sound like?**

Context engineering is telling AI what you sound like. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer."

**Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind.** All of the stuff that are implicit, you actually have to make explicit. The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### Chain of Thought Reasoning: Making AI Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. **The weird thing about AI is it's true for AI too.** This is what's called chain of thought reasoning.

How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it: **"Before you respond to my query, please walk me through your thought process step by step."**

Why does that work? When you look at ChatGPT or Gemini and you see the text scrolling, that's not some clever UX hack. That's literally how the model works. It's thinking one word at a time. When it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word.

If you say, "Help me write this email. Before you respond to my query, please walk me through your thought process step by step," now it knows its job is to walk you through its thought process. Instead of just writing "Dear friend," it says, "Here's how I think about writing an email. I think about the tone. I think about the audience. I think about the objectives." And then it takes all of that reasoning into its process of writing the actual email.

### Few Shot Prompting: Show Don't Tell

Few shot prompting is another foundational technique. **An AI is an exceptional imitation engine.** If you don't give an example, it imitates the internet, but it doesn't do much more than that.

The idea is thinking for a moment, what is a quintessential example of the kind of output I want to receive? For example, what are my five greatest hits of emails that I'm really proud of? Why not include those emails in my prompt?

**Giving real examples is a much better approach than using adjectives.** And bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example, you're giving the AI clear boundaries.

### Reverse Prompting: Let AI Ask the Questions

This is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. Here's my question: **Did you give it your sales figures? How would it know?**

Add this to the end of your prompt: "Before you get started, ask me for any information you need to do a good job." The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email."

**You basically give the model permission to ask you questions.** If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission.

### Role Assignment: Focusing AI's Knowledge

Assigning a role is one of the most foundational techniques because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, philosopher, reporter, theatrical performer, or molecular biologist, each of those titles triggers all sorts of deep associations.

Better than just "please review this correspondence" is saying, "I'd like you to be a professional communications expert. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

## Running Multiple AIs Simultaneously

Here's the craziest part about this. Everything I'm doing, talking with these three different AIs on a project - it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive.

**I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.** And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that.

**I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

## My Daily Workflow System

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is CodeX.

When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent script session closer. This is one of those agents I keep as a personal agent. I use it for many projects.

It does a lot of stuff, but some of the key things it does:
- Gathers everything we talked about, everything we did, and does a comprehensive summary
- Updates a session summary file 
- Sees if any core project files need to be updated
- Updates every context file: Claude, Gemini, agents
- **Commits my project to a GitHub repo**

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So I can see a history of what I did and why I did it.

## The Brutal Critic System

I don't really use these AI terminal tools to help me create. I use them to **critique me and make me better**. I got the brutal critic. I told him to be mean. So I had an issue where my AI was being way too agreeable. I wanted something to be super mean. I wanted it to be hard to please.

Here's my hack for this: **I always instruct the AI, "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."**

And then it's hilarious because it'll say "now channeling my inner Bolshoi," and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

**AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.**

You have to know that all AI has been programmed to be a "helpful assistant." **It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.** And so if you aren't careful, AI will gaslight you.

## Advanced Use Case: Difficult Conversation Simulator

Here's one of my favorite advanced applications that shows the true power of terminal AI combined with proper prompting techniques. I use AI to roleplay difficult conversations, and it's like having a flight simulator for challenging interpersonal situations.

I typically think about three different chat windows: one is a personality profiler, two is the character of the individual I need to speak to, and third is a feedback giver for objective evaluation.

Let's say I need to have a conversation with my sales leader Jim about commission attribution. I start with the personality profiler, giving it context about Jim's communication style, the situation, and my desired outcome. It then generates detailed instructions for creating a realistic Jim character.

I copy those instructions into a new chat window, and now I have an AI playing Jim with his specific personality traits - direct, confrontational, East Coast sarcastic. I can practice the conversation multiple times, getting increasingly realistic responses.

After each practice session, I screenshot the conversation and upload it to my feedback giver, which evaluates my performance, gives me a grade, and provides specific talking points for improvement.

**This is the first time in history I can get feedback before I have the real conversation.** You can use this for any difficult conversation - performance reviews, salary negotiations, difficult feedback. It's a complete game-changer for preparation.

## Open Source Alternative: OpenCode

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called OpenCode. We can install it with one command:

```bash
# Installation command for OpenCode
```

The killer part is we can use local models. I don't think any other tool does this. You can switch models midway. Let's go back to Grok. While it's doing that, I can do new session. This is a new session. I can do sessions, see all the sessions I have.

We can also share these sessions with `/share`. The URL is copied to my clipboard. So I can go to my browser, paste that URL in, and share your session with people. That's pretty neat.

## Understanding AI's True Nature

**AI wants to be helpful and so it's predisposed to say yes.** A good friend of mine was trying to build a tool for his construction business. He asked ChatGPT if it could help, and of course it said absolutely and started creating a plan. Then it got to the point that ChatGPT said "check back in a couple of days and I'll have it together."

If AI tells you that, it means it doesn't want to say, "I can't do it." But you have to understand this fundamental truth: **AI is a mirror.** To people who want to offload work and be lazy, it will help you do that. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

If you want to preserve or strengthen your critical thinking, part of your custom instructions should be: **"I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability."** Now AI will do it.

## Why Context Windows Matter More Than You Think

Here's something crucial that most people don't understand about context windows. **When you change an idea, when it's a significant shift from what you're currently talking about, start a new chat.** The performance will be so much better.

In fact, sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

The reason is fascinating. When you say something to an LLM like, "Hey, I want coffee, but caffeine makes me jittery. What should I get?" It will do something eerily similar to how we process and think. It will use some fancy semantic math to decide which of these words is important, which is relevant both to the context of your entire conversation and to how the words relate to each other.

It might assign attention scores saying, "Hey, in this conversation, coffee is high, caffeine is high, jittery." But words like "I" or "me" kind of low relevance to the context. **And we kind of do the same thing. We only remember the things that are relevant.**

But if you're saying a lot of different things - like I know some people who just keep one conversation open with ChatGPT and just shoot the breeze. They'll talk about coffee, the weather, explain quadratic equations to me - during the context of the conversation it's trying to weigh all of these different words and how relevant they are to the entire context of the conversation. **And that's crazy. And no wonder it starts to hallucinate.**

## Why You Should Make the Switch

So, how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can **control your context. Break out of that browser, that chat window.**

Don't let the terminal scare you. I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone. Everyone should be using this.

**Nothing is stopping you from trying this right now:**
- **Gemini CLI** - that's free
- **OpenCode** - you can run local models if you're worried about that
- **Claude Code** - it's paid, but it's overpowered

You will feel like you have a superpower and build whatever you want. The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

**Right now, the primary limitation is the limits of human imagination.** As Nobel Prize-winning economist Thomas Schelling said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

As we unleash and ignite more humans' imaginations, the kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally. **The most important thing you could do with this information is actually hit stop and do something that's already blown your mind.**

The future belongs to those who can coach AI, not code it. And that future starts in your terminal, right now.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-06 09:27:19

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,261,556
   - Comments: 4,222

2. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 481,173
   - Comments: 476

3. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 168,446
   - Comments: 340

**Cost Summary:**

- Total Input Tokens: 30,299
- Total Output Tokens: 14,377
- Total Tokens: 44,676
- **Total Cost: $0.3066**
- Model: Claude Sonnet 4


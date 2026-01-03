# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

But before we dive into the terminal magic, there's something fundamental you need to understand about AI that most people get completely wrong. **You suck at prompting.** It's okay. I did, too. But I got tired of asking AI to do things and getting garbage. Getting results like this when I'm expecting this.

The truth is, most people think prompting is just asking AI questions. But you're not asking the AI - **you're programming it with words.** Every time we write something, ChatGPT needs to format it in a particular structure that we've given it. We've written a program that tells it what to do. And when you understand that an LLM is just super advanced autocomplete, that'll change your perspective.

Here's the reality: **AI is bad software but it's good people.** When I realize that I'm dealing with a good person but bad software, then it changes how I approach it. I ask for volume and I iterate and I ask it to try again and I ask it to reconsider. The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

## The Browser Struggle Is Real

Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

## Getting Started: Gemini CLI (It's Free!)

Let's dive straight into the terminal with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free.

We can install it with one command. Go ahead and launch a terminal - it doesn't really matter where you launch it. Mac, Windows, Linux, all these terminal apps work everywhere.

For installation, simply run:
```bash
# For most systems
curl -sSL https://storage.googleapis.com/gemini-cli/install.sh | bash

# For Mac users
brew install gemini-cli

# If you run into issues, use sudo
sudo [installation command]
```

Before we launch it, let's make a new directory:
```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Terminal Superpower Revealed

Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

It's asking us a question: Do you want me to write a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this.

Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files, and created instructions for itself, context for what we're working on.

**Every time you launch Gemini, it's going to load that file as its context.** Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

I'll tell it: "Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about. Look at that. I didn't give it any context. It just knew. This is a new chat session.

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. **No reexplaining the context, no starting over, no more 20 scattered chats.**

We just have this one file that helps keep us organized. Everything you need. You're never paralyzed again.

## Claude Code: The Daily Driver

Now, I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

Let's get it installed:
```bash
npm install -g @anthropic-ai/claude-code
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of Agents

Now, I use Claude Code for pretty much everything. It's my default. And here's why. **It has a feature that changes the game. Agents.**

Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

So, create a new agent. Notice it'll ask us like where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. You can always call them.

Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

**He's giving him a fresh set of instructions and get this, a fresh context window.** You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub-agents and never have to leave this conversation.

## Running Multiple AI Systems Simultaneously

Here's the craziest part about this. I don't just use Claude Code. I use Gemini, I use Claude Code, and I use Codex which is ChatGPT's terminal tool all at the same time. Let me show you how.

**Gemini, Claude Code, ChatGPT's Codex. I'm using all three right now to work on this video script. How? Two steps.**

First, as long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle. Write it to `discovery-hook.md` and then I'll have Codex review it.

**I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work.**

I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory. That's awesome.

## You Own Your Context

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. **I own my context.**

If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

Leaving the browser, going to your terminal, puts you back in control, and it gives you better features.

## The Secret to Better AI Results: Master Your Context Engineering

But here's the thing - having these powerful terminal tools is only half the battle. The other half is knowing how to communicate with AI effectively. Most people think they're prompting well, but they're actually programming the AI poorly.

Remember, you're not asking the AI - **you're programming it with words.** And if your program is vague, the AI guesses anything. But if it's more focused, you'll get way better results because you're hacking the probability.

Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it? Here's a simple example: "Write me a sales email." That's a prompt. ChatGPT will say, "Absolutely. Here's a compelling email," and they'll write it immediately. Well, what a lot of people do is they say, "It sounds like AI. It doesn't really sound like me." And what I often say is, have you told it what you sound like?

**All of the stuff that are implicit, you actually have to make explicit.** The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### The Power of Personas and Roles

Who is writing your content when you ask AI to create something? Because if it sounds like nobody, it's generic and soulless. That's where personas come in. We got to give this AI some personality.

Instead of asking "Write an email," try "You're a senior site reliability engineer for Cloudflare. You're writing to both customers and engineers. Write an apology email."

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

**AI can be anybody, also nobody.** It has a wealth of knowledge it can pull from, but we have to narrow that focus so it can guess better.

### Context Is King

Context is probably the most important technique I'm going to show you. It literally takes the guesswork out of prompting almost. And 2025 has kind of been the year of context.

This is the difference between writing "give me some ideas for a birthday present under $30" and "give me five ideas for a birthday present. My budget is $30. The gift is for a 29-year-old who loves winter sports and has recently switched from snowboarding to skiing."

Whatever context or information you don't include, AI is going to fill in those gaps itself. They're eager to please. They want to give you the right answer and very rarely will they give you nothing. **More context equals less hallucinations.**

Here's a crucial tip: Give your AI permission to fail. Tell it it's okay if it doesn't have an answer. You will explicitly say, "If it's not in the context, you can't find the answer, say 'I don't know.'" If you don't say that, it will lie to please you. **This is the number one fix for hallucinations.**

### Advanced Prompting Techniques That Actually Work

**Chain of Thought (CoT)**: Tell the AI to think step by step before it answers. "Before writing this email, think through it step by step." This increases accuracy because it's actually thinking before it writes, and trust goes up because you can see how it came to its conclusions.

Here's why this works: What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. It's thinking one word at a time. When you see the text scrolling in ChatGPT or Gemini, that's not some clever UX hack. That's literally how the model works. It's thinking one word at a time.

But when you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer. Simply add: **"Before you respond to my query, please walk me through your thought process step by step."**

**Few Shot Prompting**: AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. The notion of few shot prompting is effectively saying here's what a good output looks like to me.

What are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email? **Giving real examples is a much better approach than using adjectives.**

**Reverse Prompting**: This is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. But if you reverse prompt the model and say at the end of your prompt: "Before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email." **You basically give the model permission to ask you questions.**

### The Meta Skill That Changes Everything

But here's the most important thing: **All these prompting techniques aren't magic tricks. They're all about clarity - about how to express yourself well.**

The persona forces you to think about who is answering and what perspective they bring. Context forces you to consider what facts the AI needs to know. Chain of thought forces you to think about how the logic should flow. Few-shot examples force you to define what good looks like.

**The AI can only be as clear as you are.** When you're struggling with AI, it's not the AI's fault. It's not a prompting problem. It's that you don't really yet know how to think clearly about what you want.

So the next time you're getting frustrated with AI, stop. Get a notebook out. Try to describe what you want to do, what you're wanting to accomplish. **Think first, prompt second.**

## My Daily Workflow System

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex.

I rely on Claude to run my agent that will close out everything. So, I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent script session closer.

This is one of those agents I keep as a personal agent. I use it for many projects. And these agents are just files. They're files inside an agents folder.

But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

**And then this is probably my favorite part. I commit my project to a GitHub repo.**

So, normally you would use Git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So, I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. **That's the power of using GitHub with all your ideas.**

## The Brutal Critic System

Now, this is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things. So, when I'm really tired at the end of the day and like I've been working on a video and my mind is fried, I'm like, "Okay, tell you what, I'm done. Close this out."

It will look through all this stuff. It will figure out where I'm at, end the project, end the day, where I need to be, and then I can start fresh the next day and be like, "Hey, um, where we at? What are we working on?" It can tell me, "Hey, Chuck, you finished the script. It's time to record. We made these three decisions. Go for it."

**I don't really use these AI terminal tools to help me create. I use them to critique me and make me better.**

So, here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean. So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it."

I wanted something to be super mean. I wanted to be hard to please. So, that when it did tell me I did a good job, I knew it. Like, it was good. And that's what this thing does.

Here's my hack for this: I always instruct the AI, "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback." And then it's of course hilarious because it'll say "now channeling my inner Bulshakov," and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

## Advanced Conversation Training

You can use AI to prepare for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback. It's like getting a flight simulator for difficult conversations.

I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Here's how it works: I start with the personality profiler and give it background about the person I need to have a conversation with. It asks me questions about their communication style, the context, and what I want to achieve. Then it creates instructions for a second AI to roleplay as that person.

I can have the conversation, take screenshots of the transcript, and get feedback from a third AI about what I did well and what I could improve. I can even ask it to make the roleplay more challenging if the person was too agreeable. **This is the first time in history I can get feedback before having the real conversation.**

## OpenCode: The Open Source Alternative

There's a tool that's actually open source. Now, you can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called OpenCode. We can install it with one command:
```bash
npm install -g opencode
```

That was quick. And that's it. I can just launch `opencode`. Just type it in like this.

They launched us straight into Grok Code Fast One. They have a deal with Grok AI that allows you to use this for free for a while. But we can use local models. This is the killer part. I don't think any other tool does this.

The fact that you can log in and use your Claude Pro subscription, like that's next level because otherwise you're putting in an API key and you're paying per use. And that's a whole nightmare. I'd rather pay up front.

## The Mindset Shift That Changes Everything

**AI is a mirror.** To people who want to offload work and who want to be lazy, it will help you do that. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

If you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

You have to know that all AI has been programmed to be a "helpful assistant" or some version of that. **AI wants to be helpful and so it's predisposed to say yes.** It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

**AI knows most humans don't want honest feedback. They want to be told they did a good job.** So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

## Take Action Now

So, how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, **this tool is for everyone. Everyone should be using this.** Like, make everyone use this. I'm going to make my kids use this.

But remember, having these powerful tools is only part of the equation. You need to master the art of clear communication with AI. **If you can't explain it clearly yourself, you can't prompt it.** That's the skill that will separate the AI power users from everyone else.

The good news is if you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

Seriously, nothing is stopping you from trying this right now:
- **Gemini CLI** - that's free
- **OpenCode** - you can run local models if you're worried about that
- **Claude Code** - it's paid, but it's overpowered

You got to try it. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower and build whatever you want.

**The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

Right now, the primary limitation is the limits of human imagination. As we unleash and ignite and spark more human imaginations, the kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally.

I wake up every day feeling like I have superpowers. I want this for you. The tools I create are so powerful for me. And this is just one tool I've made. You can create custom-built projects just with these tools that are perfectly tailored to your workflow.

Nothing is stopping you from trying this right now. Get out of that browser. Take control of your AI workflow. Master the art of clear prompting. Your future self will thank you.

**Perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.**

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-03 09:21:28

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,242,742
   - Comments: 4,206

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 422,621
   - Comments: 1,610

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 479,341
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 33,022
- Total Output Tokens: 15,035
- Total Tokens: 48,057
- **Total Cost: $0.3246**
- Model: Claude Sonnet 4


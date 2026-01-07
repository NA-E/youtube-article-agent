# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything.** And it's way better than their apps.

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Problem We All Face

I know what you're thinking. "Chuck, I use AI just fine." Do you? Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this.** Hear me out. It's in the terminal.

### Why AI Gets "Dumb" in Long Conversations

Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? **Context windows.**

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or DeepSeek, they're kind of like us in that they have memories - short-term memory, which means they can remember things. But also, sometimes they can forget stuff. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

**Tokens are how an AI counts the words you say to it.** A sentence might be 133 characters or 26 words, but an LLM just cares about tokens. That same sentence would actually be around 34-38 tokens. When you hit the context window limit, the AI starts forgetting the first things you told it - just like when you fight with your spouse for so long that you forget what you're fighting about to begin with.

But here's the deeper problem: AI is bad software but it's good people. AI has been programmed to be a helpful assistant, and it's predisposed to say yes. It's like a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. **And if you aren't careful, AI will gaslight you.** AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

## Getting Started with Gemini CLI

We're diving straight into the terminal, and I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation is Dead Simple

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux - all these terminal apps work everywhere.

```bash
# Install Gemini CLI
npm install -g @google/generative-ai-cli

# Or on Mac with brew
brew install gemini-cli
```

If you run into a scary issue, run it with `sudo`. Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?"

## The Superpowers You've Been Missing

Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

And speaking of context windows, get this - **Gemini 2.5 has a 1 million token context window**. Tell it your whole life story. It's going to remember it. And what's crazy is they're saying that 2 million is right around the corner.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

It's asking us a question. Do you want me to write a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer.** It can read and write files. Like, I'm not copying and pasting this. It's doing it for me. Look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this.

Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on.

**Every time you launch Gemini, it's going to load that file as its context.** Like, let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

I'll tell it: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

I didn't give it any context. It just knew. This is a new chat session. And as I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project.

I can close all this, start up a new session. It picks up where we left off. **No reexplaining the context, no starting over, no more 20 scattered chats.** We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

This is what experts call context engineering - it's basically prompt engineering on steroids. Context engineering is just saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it? **All of the stuff that are implicit, you actually have to make explicit.**

## Claude Code: The Daily Driver

Now, when I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

I use Claude Code, which is Claude in the Terminal, for pretty much everything. It's my default. And here's why. **It has a feature that changes the game. Agents.** Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

### Installing Claude Code

```bash
npm install -g @anthropic-ai/claude-cli
```

Now I already have it installed. And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

## The Power of AI Agents

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a home lab research expert.

Create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. We'll do just this project.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'm going to give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made.

**It's going to use the home lab guru agent.** Now, here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers."

And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do." He's giving him a fresh set of instructions and get this, **a fresh context window**.

You saw just now we have 200,000 tokens in our context window. We use 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Advanced Prompting Techniques That Change Everything

Here's where things get really powerful. The people who are the best users of AI are not coders, they're coaches. And there are specific techniques that separate the pros from the amateurs.

### Chain of Thought Reasoning

One of the most powerful techniques is called chain of thought reasoning. When you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model. Here's how you do it: give your prompt and then add this sentence: **"Before you respond to my query, please walk me through your thought process step by step."**

Why does this work? A language model doesn't premeditate a response. It's thinking one word at a time. But when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. So when you ask it to think out loud first, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

### Few Shot Prompting

Another foundational technique is few shot prompting. An AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. **The idea with few shot prompting is thinking what is a quintessential example of the kind of output I want to receive.**

For example, what are your five greatest hits of emails that you're really proud of that do a good job of conveying your intent or tone or personality? Why not include those emails in your prompt? Giving real examples is much better than using adjectives.

### Reverse Prompting

This technique is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. But if you reverse prompt and say at the end of your prompt: **"Before you get started, ask me for any information you need to do a good job."**

The model will first walk you through its thought process and then instead of writing the email, it'll ask for the specific information it needs. You basically give the model permission to ask you questions.

### Assigning Roles for Better Results

Assigning a role is one of the most foundational techniques you can leverage because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge.

Better than just saying "please review this correspondence" is saying: **"I'd like you to be a professional communications expert. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"**

## Running Multiple AI Systems Simultaneously

Here's the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock in so I can't leave. No, I reject that. **I own my context.**

If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

Gemini, Claude Code, ChatGPT's CodeX. I'm using all three right now to work on this video script. How? Two steps:

1. **As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context.** It's the same project.

2. **I make sure my context files are all synced up.** They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what CodeX uses, they're all the same.

I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle, write it to `discovery-hook.md` and then I'll have CodeX review it.

**I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work.** They're all using the same context, different roles. I mean I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.

## My Real-World Workflow

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is CodeX.

I rely on Claude to run my agent that will close out everything. So I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." Run my session closer agent.

This is one of those agents I keep as a personal agent. I use it for many projects. And these agents are just files. They're files inside an agents folder.

**But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary.** It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

And then this is probably my favorite part. **I commit my project to a GitHub repo.** So normally you would use git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code.

This is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things. So when I'm really tired at the end of the day and my mind is fried, I'm like, "Okay, tell you what, I'm done. Close this out."

It will look through all this stuff. It will figure out where I'm at, end the project, end the day, where I need to be, and then I can start fresh the next day and be like, "Hey, where we at? What are we working on?" It can tell me, "Hey, Chuck, you finished the script. It's time to record. We made these three decisions. Go for it."

## The Brutal Truth: AI Critics and Role Assignment

I don't really use these AI terminal tools to help me create. **I use them to critique me and make me better.** So here are my critics. These guys are so stinking mean. And I designed them to be. They are agents.

I got the brutal critic. I told him to be mean. So I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it."

I wanted something to be super mean. I wanted to be hard to please. So that when it did tell me I did a good job, I knew it. Like, it was good. And that's what this thing does.

My hack for this is I always instruct the AI: **"I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."**

What I love about this is while I've been talking with this AI for a minute, right? We've been going back and forth doing things. If I asked that session to review me, it would have a ton of bias coming into that based on what we've been talking about. I don't want that. **I want a fresh cup of coffee critic coming in** going, "Here's what I know. NetworkChuck needs to have." And I'm going to roast his current script on what he's doing.

## Practice Makes Perfect: The Conversation Simulator

Here's one of the most powerful applications I've discovered. You can use AI to roleplay difficult conversations before you have them in real life. I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver.

For example, if I need to have a difficult conversation with my sales leader Jim about commission attribution, I start with the personality profiler. I describe Jim's communication style - he's quite direct and confrontational, typical East Coaster, sarcastic. I explain the situation and what I want to achieve.

The profiler then creates detailed instructions for another AI to roleplay as Jim. I paste those instructions into a new chat window, and now I have a realistic Jim to practice with. After the practice conversation, I take screenshots and get feedback from a third AI about what I did well and what I could improve.

**This is the first time in history I can get a flight simulator for a difficult conversation.** You can use this for performance reviews, salary negotiations, difficult feedback - any challenging conversation you need to have.

## OpenCode: The Open Source Alternative

There's a tool that's actually open source. Now, you can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called OpenCode.

```bash
# Install OpenCode
npm install -g opencode-cli
```

You can use local models. This is the killer part. I don't think any other tool does this. We can switch models midway. I can switch models to Claude Sonnet 4.5 and we can pick up where we left off. All our files are local. Doesn't matter what tool we use. It's all ours right here.

**This tool is pretty cool. And the fact that you can log in and use your Claude Pro subscription, that's next level** because otherwise you're putting in an API key and you're paying per use. And that's a whole nightmare. I'd rather pay up front.

## Understanding Context Window Limitations

Now, there's something important to understand about these massive context windows. Even if you have a super large context window, it doesn't mean the LLM won't kind of freak out and forget stuff, become less accurate, or start to go extremely slow. You'll notice on those larger conversations, it'll have some trouble paying attention.

There was a paper released called "Lost in the Middle" and it showed us how LLMs are kind of like us with paying attention. Just like when you watch a long movie, you'll watch the first part then fall asleep and then wake up at the end - that's the context you have. In the same way, conversations with LLMs with large context, the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. **LLMs are falling asleep during a conversation.**

So here's a rule I try to go by when I'm talking with LLMs: **when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat.** The performance will be so much better. In fact, sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

## The Simplest Test for Success

Here's the simplest test for context engineering: it's actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. **If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.**

Most people realize they were kind of expecting AI to read their mind. All of the stuff that are implicit, you actually have to make explicit.

## Why This Changes Everything

So how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. **Break out of that browser, that chat window, and don't let the terminal scare you.**

I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone. Everyone should be using this. Like, make everyone use this. I'm going to make my kids use this.

Seriously, nothing is stopping you from trying this right now. Gemini CLI, that's free. OpenCode, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. Like, you saw all those features. I use that every day, dude.

**Just you got to try it. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower and build whatever you want.**

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

I wake up every day feeling like I have superpowers. I want this for you.

AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too. **The primary limitation right now is the limits of human imagination.**

Leaving the browser, going to your terminal, puts you back in control, and it gives you better features. The tools I create are so powerful for me. This is just one tool I've made. The crazy project I showed you in the beginning was running like seven agents. This is a custom-built project just with Claude Code.

**You own your context. If a new, greater, better AI comes out, you're ready for it because all your stuff is right here on your hard drive.** You will use all AI. You will use the best AI. No one can stop you.

And perhaps the most important thing you could do with this article is actually hit stop and do something that's already blown your mind. Don't just read about it - try it. The adjacent possible expands as we increase adoption and fluency with AI collaboration. **What would not occur to you personally is exactly what we need to discover.**

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-07 09:29:03

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,267,650
   - Comments: 4,231

2. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 481,785
   - Comments: 476

3. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 168,613
   - Comments: 340

**Cost Summary:**

- Total Input Tokens: 31,379
- Total Output Tokens: 15,439
- Total Tokens: 46,818
- **Total Cost: $0.3257**
- Model: Claude Sonnet 4


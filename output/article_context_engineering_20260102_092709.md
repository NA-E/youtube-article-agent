# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

But before we dive into the terminal superpowers, we need to talk about something crucial: **You suck at prompting.** It's okay. I did, too. But I got tired of asking AI to do things and getting garbage. Getting results like this when I'm expecting this. Like, have you ever yelled at ChatGPT? Like really insulted it? Because you're so frustrated with the results.

If you haven't, you're not using it enough. It's those moments, that frustration that makes me think one of two things. One, AI is dumb and I'm not going to use it anymore. Those naysayers are right. Or two, I'm dumb and I have no idea how to use AI. I most often feel like option two.

The problem is that most people, including me, get prompting fundamentally wrong. **You aren't asking the AI. You're programming it with words.** Every time we actually write something, ChatGPT needs to format it in a particular structure that we've given it. We've wrote a program that tells it what to do.

## The Browser Struggle is Real

I know what you're thinking. "Chuck, I use AI just fine." Do you? Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this.** Hear me out. It's in the terminal.

But first, let's fix your prompting because even the most powerful terminal tools won't help if you can't communicate effectively with AI.

## Understanding AI's True Nature

Here's something critical you need to understand: **AI is bad software but it's good people.** I joke about this, but it's true. When I realize that I'm dealing with a good person but bad software, it changes how I approach it. I ask for volume, I iterate, I ask it to try again, and I ask it to reconsider.

You have to know that at its basic level, **AI wants to be helpful and so it's predisposed to say yes**. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. They're not really great at setting boundaries. And so if you aren't careful, AI will gaslight you.

A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said check back in a couple of days and I'll have it together. And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

If AI tells you that, it means it doesn't want to say, "I can't do it." But you have to remember - **the people who are the best users of AI are not coders, they're coaches.**

## The Secret to Better Prompting

Here's what I learned after going deep - too deep. I took all the top prompting courses on Coursera. I read all the official prompting docs, Anthropic, Google, OpenAI. And then I asked all the experts, the best prompt engineers I know.

**You need to understand what prompting really is.** Prompting essentially is just asking AI to do stuff. And it almost feels like talking to a human. Sometimes we forget that it's not. But you have to remember you're talking to a computer.

A prompt is a call to action to the large language model. It's a call to action. But a prompt just isn't a question. **It's a program.** You aren't asking the AI. You're programming it with words.

LLMs don't think like we do. They are prediction engines. When you understand that an LLM is just super advanced autocomplete, that'll change your perspective. **You're not asking a question. You're starting a pattern.** If your pattern is vague, the AI guesses anything. But if it's more focused, you'll get way better results because you're hacking the probability.

### Context Engineering: The Game Changer

Context engineering - the first time I heard about it was when Andre Karpathy tweeted about it. I think probably Toby Lutke, the CEO of Shopify, also referenced it as well. I started digging into it. It's kind of just an evolution of prompt engineering. Really, **context engineering is just prompt engineering on steroids**.

It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it? Here's a simple example: "write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, you know, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like?

**Context engineering is telling AI what you sound like.** If you say, "Write me a sales email," it will. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email.

Your goal is to have an output as reliable per your specification as possible. But **AI can't read your mind**. And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind."

All of the stuff that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity. **Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.**

### The Power of Personas

Who is writing your content when you ask AI to write it? And no, it's not a call center of people, but what's the perspective? Because generic prompts sound like nobody. They're generic and soulless. That's where personas come in. We got to give this AI some personality.

Instead of just asking for an apology email, try: "You're a senior site reliability engineer for Cloudflare. You're writing to both customers and engineers. Write an apology letter or email."

**AI can be anybody, also nobody.** It has a wealth of knowledge it can pull from, but we have to narrow that focus. Persona refers to what expertise you want the generative AI tool to draw from. Get to narrow its focus so it can guess better.

**Assigning a role is one of the most foundational techniques** because it's effectively telling the AI where in its knowledge it should focus. So very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

### Context is King

This is probably the most important technique I'm going to show you. It literally takes the guesswork out of prompting almost. And 2025 has kind of been the year of context. Like context is king.

Whatever context or information you don't include, it's going to fill in those gaps itself. This is kind of the downside of LLM. They're eager to please. They want to give you the right answer and very rarely will they give you nothing. **So more context equals less hallucinations.**

**Never assume it knows something. Never assume it has all the context. Always provide all the context every time.** ABC. Always be contexting. You're not going to know what it knows. So, always tell it what you want it to know.

Here's a trick I learned from Anthropic: **Give your AI permission to fail.** Tell it it's okay if it doesn't have an answer. Give it permission to say, "I don't know." You will explicitly say, "If it's not in the context, you can't find the answer, say, 'I don't know.'" If you don't say that, it will lie to please you. And this is the number one fix for hallucinations.

AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job. **My kind of hack for this is I always instruct the AI, I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback.**

## Advanced Prompting Techniques

### Chain of Thought: Making AI Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves.

**The weird thing about AI is it's true for AI too.** This is what's called chain of thought reasoning. And when you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model.

So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: **"Before you respond to my query, please walk me through your thought process step by step."** That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. **A language model does not premeditate a response to you.**

So, if you say, for example, help me write this sales email. It doesn't say, what's a good sales email? Here it is. It's thinking one word at a time. But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word.

When you ask a model to think out loud or use chain of thought reasoning, **it gives the model the opportunity to bake all of its thought process about the task into its own answer**. By asking a model to think out loud, you know the answer to what are all of the assumptions that the model baked into its answer.

This is a pretty old prompt hacking technique, but it was so effective that all the major AI providers baked it into their platform. Look for buttons like "extended thinking" or "thinking" - when a model can do this they're called reasoning models and they're powerful.

### Trees of Thought: Multiple Paths to Success

This next one is incredibly fun. It's called ToT or trees of thought. So, where CoT explores one linear path, ToT explores multiple paths at once, like branches going on a tree. It's like going through a maze. Your goal is to get to the end, but you may have to follow a couple of different paths before you get there.

With problem solving, especially complex problems, the first idea isn't always best. So, it enables the AI to do self-correction. It can go down one path and go, "Oh, dead end." Go down this path. "Oh, that's a good one." Try this path. "Oh, that one's better." It generates a diversity of options.

### Few Shot Prompting: Show Don't Tell

Few shot prompting is another very important technique. It's a foundational technique. You could say it's a predecessor to this kind of modern obsession with context engineering. **The idea with few shot prompting is an AI is an exceptional imitation engine.**

If you don't give an example, it imitates the internet, but it doesn't do much more than that. And the notion of few shot prompting is effectively saying here's what a good output looks like to me. The idea with few shot prompting is thinking for a moment, what is a quintessential example of the kind of output I want to receive.

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality or whatever it is? **Why not include those emails in my prompt for an email?**

If you don't give any guidance, it's going to sound like whatever it thinks the average kind of response or the average output should sound like and most of the time its intuition is wrong. **Giving real examples is a much better approach than using adjectives.**

Bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example. Somebody might say good example is easy but bad examples hard. It's only hard to the unaugmented person. If you have AI augmentation, which we now all do, you can say to an AI, I'm trying to few shot prompt a model. I've got a good example, but I struggle even to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few shot prompt?

### Reverse Prompting: Let AI Ask the Questions

The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically **asking the model to ask you for the information it needs**.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt, you know, help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. **And before you get started, ask me for any information you need to do a good job.**

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

**You basically give the model permission to ask you questions.** This is part of the core actually of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. Any good manager - imagine a manager who says, "Don't ask me any questions." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

### The Playoff Method: Battle of the Bots

Let's get even crazier. The community calls this one the playoff method. Researchers call it adversarial validation. I call it battle of the bots. Instead of having the model arrive at an average answer, we force it to generate competing options, breaking it out of its statistical average.

With this, we're generating a three round competition with three distinct personas. We got the engineer, the PR crisis manager, the angry customer. Round one, the engineer and the PR crisis manager write their own version. The angry customer reads both drafts and brutally critiques them. And then they read the customer's feedback and then collaborate to produce one final great result.

The reason this works is because AI is normally better at critiquing or editing than original writing. So, asking it to do this is actually tapping into its superpower.

## Getting Started with Gemini CLI

Now that you understand better prompting, let's dive straight into the terminal with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free.

You can install it with one command. Go ahead and launch a terminal - it doesn't really matter where you launch it. Mac, Windows, Linux, all these terminal apps work everywhere. 

For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux. I'll launch my Ubuntu terminal and copy and paste this command:

```bash
curl -sSL https://sdk.cloud.google.com | bash
gcloud components install gemini-cli
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

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" It's doing a Google search right now. Pretty sick. And then it responds just like we're used to.

## The Terminal Superpowers

That wasn't so bad, was it? But notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing.

Now, it's asking us a question. Do you want me to write a file for you? Do you want me to create a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on.

Let's take a look at it:

```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. **And every time you launch Gemini, it's going to load that file as its context.**

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file. And I'll tell it this:

> Write the intro for blog post one in the coffee series.

No more context. Just that. It should know exactly what I'm talking about. Look at that. I didn't give it any context. It just knew. This is a new chat session.

## Taking Control of Your Projects

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

When I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

I'm literally using the `gemini.md` file right now for this project. This is a small example. Let me show you a big one. This is the `gemini.md` file for this video. It tracks everything. It describes how I create project status, major decisions I made, even other documents it should look at.

I'll launch a whole new Gemini session in this project and I'll ask where we're at in the project. Are you seeing this? This has completely changed the way I create or do anything now.

## Claude Code: The Daily Driver

And I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

Let's get it installed with one command:

```bash
npm install -g @anthropic-ai/claude-cli
```

And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

Now again, don't be afraid. Ask Claude a question like, "I need to find a NAS for my house. Here's my budget, what I want to do. Create a report for me."

## The Power of Agents

I use Claude Code for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**. Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

So, create a new agent. Notice it'll ask us like where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. We'll do just this project. We'll use Claude to make it.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'll give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made. I can just do an @ symbol and look at the documents in our directory.

Watch. It's going to use the home lab guru agent. There it is. There's our agent researching for us right now.

## Why Agents Are Game-Changers

Now, here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

He's giving him a fresh set of instructions and get this, **a fresh context window**. You saw just now we have 200,000 tokens in our context window. We use 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated.

I can give tasks to other sub agents and never have to leave this conversation. Claude just delegated this task to a new agent. He's got a fresh pot of coffee. He's ready to go. He just walked into work.

## Running Multiple AIs Simultaneously 

Here's the craziest part about this. Everything I'm doing, talking with these three different AIs on a project - it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive. I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.

And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock in so I can't leave. No, I reject that. **I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

Gemini, Claude Code, ChatGPT's Codex - I'm using all three right now to work on this video script. How? Two steps. First, as long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle, write it to `discovery-hook.md` and then I'll have Codex review it.

I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work. They're all using the same context, different roles. I mean, I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory. That's awesome.

## Preparing for Difficult Conversations with AI

One of the most powerful applications I've discovered is using AI to prepare for difficult conversations. This is like having a flight simulator for challenging interactions.

I typically think about kind of three different chat windows, so to speak. One is a personality profiler. Two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Here's how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I'm just going to go into the tough conversation personality profiler and I'm going to say, "Hey, I'd love your help preparing for a conversation. I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler gathers intelligence about the character and the scene. It asks questions like: How would I describe Jim's communication style? What's the background of the situation? What's my best case outcome?

After profiling, I copy the instructions into a new ChatGPT window to roleplay as Jim. Then I practice the conversation, getting realistic responses based on Jim's personality profile. After the practice conversation, I can screenshot the transcript and get feedback from a third AI acting as an objective evaluator.

**This is the first time in history I can get feedback before having the real conversation.** You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback. It's a great way to basically get a flight simulator for a difficult conversation.

## Open Code: The Open Source Alternative

There's a tool that's actually open source. Now, you can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called Open Code. We can install it with one command:

```bash
npm install -g @opencode/cli
```

That was quick. And that's it. I can just launch open code. Just type it in like this. You can open and close your terminal and do the same thing.

This is open code. A nice terminal user interface. Couple things real quick. They launched us straight into Grok Code fast one. They have a deal with Grok AI that allows you to use this for free for a while.

We can use local models. This is the killer part. I don't think any other tool does this. We can also log into Claude with this command: `opencode login`. I can choose anthropic with my Claude pro. And now I'm logged into Claude code. I just launch open code now and switch models to Claude Sonnet 3.5 and we can pick up where we left off.

## My Daily Workflow System

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex.

I rely on Claude to run my agent that will close out everything. So, I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent script session closer.

This is one of those agents I keep as a personal agent. I use it for many projects. And these agents are just files. They're files inside an agents folder.

But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

And then this is probably my favorite part. **I commit my project to a GitHub repo.** So, normally you would use git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So, I can see a history of why what I did and why I did it.

## The Power of AI Critics

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. So, here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean.

So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it." I wanted something to be super mean. I wanted to be hard to please. So, that when it did tell me I did a good job, I knew it. Like, it was good.

And that's what this thing does. The brutal critic has three personalities or three people that come in and roast it from different angles. Doing stuff like this saves me hours.

It's not writing for me. I'm doing the writing because I like to keep that. I think that's important now with AI, but I do have AI like roast me, help me stay on track because I get distracted. I might make some really bad creative decisions that aren't in line with what we're trying to do.

## The Meta Skill That Changes Everything

I've shown you the foundations. I've shown you how to prompt. I've shown you some really fun techniques. But there's one meta skill that is better than them all. It also is required for them all if you want to become a really good prompter.

I had an issue this week where I was trying to build a complex AI system with my YouTube scripting framework, and it was failing hard. I got so frustrated. I was essentially yelling at Claude like I yell at ChatGPT. So I texted Daniel Mesler, one of the experts. He's a creator of Fabric, probably the best prompt engineer I know.

And he told me this. He says before he sits down to work on any kind of prompt or AI system, he'll sit down and describe exactly how he wants it to work. And he'll sit there and red team it, meaning he'll come at it from different angles and try to make sure it's robust. And he spends a lot of time in that upfront because if he does anything else, anything less than that, he'll end up getting frustrated and confused and it'll be a big mess.

**If you can't explain it clearly yourself, you can't prompt it.** And that's the key. That's the skill. I look back at my garbage prompts and they were messy because my thinking was messy.

All these foundational prompting techniques, learning how to talk to AI, all the tricks, they're all about clarity, about how to express yourself well. The persona forces you to say, who is answering this? Where's the source of knowledge coming from

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-02 09:27:09

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,237,181
   - Comments: 4,197

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 419,218
   - Comments: 1,599

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 478,589
   - Comments: 475

**Cost Summary:**

- Total Input Tokens: 34,892
- Total Output Tokens: 18,622
- Total Tokens: 53,514
- **Total Cost: $0.3840**
- Model: Claude Sonnet 4


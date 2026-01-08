# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

But here's the reality: **AI is bad software but it's good people.** When I realize that I'm dealing with a good person but bad software, it changes how I approach it. I ask for volume, I iterate, I ask it to try again, and I ask it to reconsider. You have to remember - **AI wants to be helpful.** It's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

## The Browser AI Struggle Is Real

I know what you're thinking. "Chuck, I use AI just fine." Do you? Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

But here's the thing - even when you do move to terminal AI, you're probably still making the same fundamental mistake that's been killing your results. You suck at prompting. And I did too. But I got tired of asking AI to do things and getting garbage. Getting results like this when I'm expecting this. Like, have you ever yelled at ChatGPT? Like really insulted it? Because you're so frustrated with the results.

If you haven't, you're not using it enough. It's those moments, that frustration that makes me think one of two things. One, AI is dumb and I'm not going to use it anymore. Those naysayers are right. Or two, I'm dumb and I have no idea how to use AI. I most often feel like option two.

## The Prompting Problem You Didn't Know You Had

Here's what I learned after going deep - taking all the top prompting courses on Coursera, reading all the official prompting docs from Anthropic, Google, OpenAI, and asking all the experts: **If the AI model's response is bad, treat everything as like a personal skill issue. The problem is me.**

Most people think prompting is just asking AI to do stuff. And it almost feels like talking to a human. Sometimes we forget that it's not. But you have to remember you're talking to a computer. You aren't asking the AI. **You're programming it with words.**

Every time we write something, ChatGPT needs to format it in a particular structure that we've given it. We've wrote a program that tells it what to do. When you understand that an LLM is just super advanced autocomplete, that'll change your perspective.

LLMs don't think like we do. They are prediction engines. You're not asking a question. **You're starting a pattern.** If your pattern is vague, the AI guesses anything. But if it's more focused, you'll get way better results because you're hacking the probability.

## Getting Started with Gemini CLI

We're not going to waste any time. We're diving straight into the terminal. And I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation and Setup

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux - all these terminal apps work everywhere. Great.

For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux. If you have no idea what that is, it's totally fine.

```bash
# Installing Google Gemini CLI
curl -fsSL https://ai.google.dev/gemini-api/docs/cli | sh

# Or on Mac with brew
brew install gemini-cli
```

Coffee break while that goes. And if you run into a scary issue, run it with `sudo` just like this.

Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

We're here. Now, first, isn't that logo just awesome? I love the terminal. It's so nostalgic.

First thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account. It's going to open your browser, sign in, and I'm logged in.

## The Terminal Superpower

Now, don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?"

That wasn't so bad, was it? But notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

All right. Now, it's asking us a question. Do you want me to write a file for you? Do you want me to create a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me.

I mean, look, it actually made files on our computer. There they are. `best-coffee-method.md`, `coffee-blog.md`. Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this.

Type in `/init`. Just like that. Go.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files, and yes, go ahead, buddy. Create that file for me.

What it just did there was create instructions for itself, context for what we're working on. Let's take a look at it:

```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. **And every time you launch Gemini, it's going to load that file as its context.**

Like, let's test it. So, we still have our Gemini session open. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

And I'll tell it this: "Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about. Look at that. Yep. Go ahead, buddy.

I didn't give it any context. It just knew. This is a new chat session.

## Never Lose Context Again

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. And look, it added a summary to what we were working on to our `gemini.md` file.

I can close all this, start up a new session. It picks up where we left off. **No reexplaining the context, no starting over, no more 20 scattered chats.** We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

Now, when I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

## Context Engineering: The Evolution of Prompting

Here's where things get really interesting. Context engineering - it's just prompt engineering on steroids. **Context engineering is just an evolution of prompt engineering.** It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for?

Here's a simple example. Write me a sales email. That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

**Context engineering is telling AI what you sound like.** If you say, "Write me a sales email," it will. If you say, "Write me a sales email," in line with the voice and brand guidelines I've uploaded, it will write a totally different sales email. But that's just one part of the context.

You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add that also references our product specifications which were referenced in the call.

**Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind.** And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind."

All of the stuff that are implicit, you actually have to make explicit. **The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.**

## The Four Pillars of Better Prompting

But even with this terminal superpower, you need to understand the four foundational techniques that will transform your AI interactions. These work whether you're in the browser or terminal, but they're especially powerful when combined with terminal AI's file access capabilities.

### 1. Personas: Give Your AI Personality and Focus

Who is writing your response? Because when you ask AI to write something without specifying, it sounds like nobody. It's generic and soulless. That's where personas come in. We got to give this AI some personality.

Instead of just asking for an email, try: "You're a senior site reliability engineer for Cloudflare. You're writing to both customers and engineers. Write an apology letter."

**Persona refers to what expertise you want the generative AI tool to draw from.** You get to narrow its focus so it can guess better. AI can be anybody, also nobody. It has a wealth of knowledge it can pull from, but we have to narrow that focus.

**Assigning a role is one of the most foundational techniques** that you can leverage because it's effectively telling the AI where in its knowledge it should focus. So very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

You start to appreciate why simply giving a role helps because it starts to tell the AI where in your vast knowledge bank do I want you to draw information and make connections. Better than just "please review this correspondence" is saying "I'd like you to be a professional communications expert. And if you have a favorite professional communications expert use them. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

### 2. Context: The King of 2025

Context is probably the most important technique. It literally takes the guesswork out of prompting almost. And 2025 has kind of been the year of context. Like context is king.

This is the difference between writing, "give me some ideas for a birthday present under $30," and "give me five ideas for a birthday present. My budget is $30. The gift is for a 29-year-old who loves winter sports and has recently switched from snowboarding to skiing."

**More context equals less hallucinations.** Whatever context or information you don't include, it's going to fill in those gaps itself. They're eager to please. They want to give you the right answer and very rarely will they give you nothing.

My advice: **Never assume it knows something. Never assume it has all the context. Always provide all the context every time.** ABC. Always be contexting.

Here's a trick from Anthropic's official prompting documentation: Give your AI permission to fail. Tell it it's okay if it doesn't have an answer. You will explicitly say, "If it's not in the context, you can't find the answer, say, 'I don't know.'" If you don't say that, it will lie to please you. **And this is the number one fix for hallucinations.**

### 3. Output Requirements: Your Formatting Superpower

Telling the LLM exactly how you want the result to look is kind of a superpower. Instead of just asking for something, specify exactly what you want:

- "Clear bulleted list for timeline"
- "Keep it under 200 words"
- "The tone: professional, apologetic, radically transparent, no corporate fluff"

You're seeing the power of this, right? You can even get creative: "Extremely anxious and panicked. Sound like you're afraid of getting fired. Run on sentences all lowercase."

### 4. Few-Shot Examples: Show, Don't Tell

What if instead of describing what you want, you showed the AI examples of exactly what good looks like? **Few-shot prompting** is one of the best things you can do.

**The idea with few-shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that.** The notion of few-shot prompting is effectively saying here's what a good output looks like to me.

We're not describing the output, we're showing the output. Instead of pasting entire examples, give focused snippets:
- "Here's what technical transparency looks like..."
- "Here's what a timeline looks like..."
- "Here's the tone and ownership style..."

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email?

**Bonus points if you actually give a bad example.** If you say please follow this good example and then steer clear of this bad example. Giving real examples is a much better approach than using adjectives.

This gives it much less room to guess and gives you the best results.

## Advanced Prompting Techniques That Change Everything

Now that you understand the foundations, let's get crazier with some advanced techniques that will blow your mind.

### Chain of Thought: Show Your Work

Chain of thought is like showing your work in math class. We're telling the LLM to take steps to think step by step before it answers. **One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud.**

If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. **The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning. And when you get an AI to think out loud, so to speak, meaningfully improve the outputs of the model.**

It looks like this: "Before writing this email, think through it step by step."

**How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it.** Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step." That's chain of thought reasoning.

**Why does that work? It comes back to the fundamental architecture of large language models.** What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you.

When you look at ChatGPT or Gemini or many others and you see the text scrolling, that's not some clever UX hack. That's not some cutesy design decision. **That's literally how the model works. It's thinking one word at a time.**

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. So when you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

This does two things for us. First, accuracy goes way up because it's actually thinking before it writes. Also, trust goes up because we're seeing what it's doing, how it came to its conclusions.

All the major AI providers baked this into their platforms. Look for buttons like "extended thinking" or "reasoning mode." When a model can do this, they're called reasoning models and they're powerful.

### Tree of Thought: Multiple Paths at Once

Where chain of thought explores one linear path, **tree of thought** explores multiple paths at once, like branches going on a tree. It's like going through a maze. Your goal is to get to the end, but you may have to follow a couple of different paths before you get there.

With problem solving, especially complex problems, the first idea isn't always best. So, it enables the AI to do self-correction. It can go down one path and go, "Oh, dead end." Go down this path. "Oh, that's a good one." Try this path. "Oh, that one's better."

Try this: "Brainstorm three distinct tonal strategic approaches. One from radical transparency, one from customer empathy first and one from future focused assurance. Evaluate each branch. Synthesize them and then find the golden path."

### Battle of the Bots: Adversarial Validation

The community calls this one the playoff method. Researchers call it adversarial validation. I call it **battle of the bots**. Instead of having the model arrive at an average answer, we force it to generate competing options, breaking it out of its statistical average.

Generate a three round competition with three distinct personas. Got the engineer, the PR crisis manager, the angry customer. Round one, the engineer and the PR crisis manager write their own version. The angry customer reads both drafts and brutally critiques them. Then they read the customer's feedback and collaborate to produce one final great email.

The reason this works is because AI is normally better at critiquing or editing than original writing. So, asking it to do this is actually tapping into its superpower.

### Reverse Prompting: Let AI Ask You Questions

**The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.**

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt, "help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

**So, you basically give the model permission to ask you questions.** This is part of the core actually of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me."

But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

## Claude Code: The Daily Driver

Now, I'm literally using the `gemini.md` file right now for this project. This is a small example. Let me show you a big one. This is the `gemini.md` file for this video. It tracks everything. It describes how I create project status, major decisions I made, even other documents it should look at. Yeah, it can do that.

And I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

### The Power of Agents

Now, I use Claude Code, which is Claude in the Terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game. **Agents**. Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installing Claude Code

Let's get it installed with one command:

```bash
npm install -g @anthropic-ai/claude-cli
```

And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## Creating Your First Agent

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

So, create a new agent. Notice it'll ask us like where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. You can always call them.

We'll do just this project. We'll use Claude to make it. We can tell it what we want it to be. Choose our model. Sonnet's great auto color. There's our agent. Press enter to save.

## The Agent Revolution

I'm going to do a `/context` once more so we can get our baseline. We've used 85,000 tokens. I'll give it this prompt and I'm calling it home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made.

Watch. It's going to use the home lab guru agent. There it is. There's our agent researching for us right now.

Now, here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

**He's giving him a fresh set of instructions and get this, a fresh context window.** You saw just now we have 200,000 tokens in our context window. We use 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated.

I can give tasks to other sub agents and never have to leave this conversation. Claude just delegated this task to a new agent. He's got a fresh pot of coffee. He's ready to go. He just walked into work.

## Preparing for Difficult Conversations with AI

Here's something powerful you can do with these AI systems that most people never think of - **use AI to roleplay difficult conversations.** I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Let me show you how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I'll go into the tough conversation personality profiler and say, "Hey, I'd love your help preparing for a conversation. I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler will gather intelligence about the character and the scene, asking questions like: How would I describe Jim's communication style? What's the best case outcome of this conversation?

Then I copy the instructions into a new ChatGPT window where Jim comes to life as a character. I can practice the conversation multiple times, getting increasingly realistic responses. After each conversation, I can screenshot the transcript and get feedback from a third AI window that evaluates how I did.

**This is the first time in history I can get a flight simulator for a difficult conversation.** You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback.

## Multiple AI Systems Working Together

But here's the thing. I don't just use Claude code. I use Gemini. I use Claude code and I use Codex which is ChatGPT's terminal tool all at the same time. Let me show you how.

Gemini, Claude code, ChatGPT's Codex. I'm using all three right now to work on this video script. How? Two steps.

First, as long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

And I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle. Write it to `discovery-hook.md` and then I'll have Codex review it.

And that's normally what I do. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work.

**I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.** That's awesome.

## You Own Your Context

Now, are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference.

Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock in so I can't leave. No, I reject that. **I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive.

I will use all AI. I will use the best AI. No one can stop me.

## My Daily Workflow System

So, I got a little excited there. And that's what I want you to take away here. Leaving the browser, going to your terminal, puts you back in control, and it gives you better features.

But now, I want to get real practical. I want to show you exactly how I run a project like this. How I keep things in sync, how I keep my Claude, Gemini, and agents files in sync and work on a daily basis using a system like this.

### The Session Closer Agent

When I'm done for the day, I'll go, "Hey, let's close this out." Run. And I'll mention my agent script session closer. This is one of those agents I keep as a personal agent. I use it for many projects.

And these agents are just files. They're files inside an agents folder.

But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

And then this is probably my favorite part. **I commit my project to a GitHub repo.** So, normally you would use git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code.

We commit that change, give a reason for that change. So, I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. **That's the power of using GitHub with all your ideas.**

## The Brutal Critics

Now, this is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things.

The syncing is probably my favorite part. No, no, actually, this thing is my favorite part. How it roasts me. So, I don't really use these AI terminal tools to help me create. **I use them to critique me and make me better.**

So, here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean.

So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it."

I wanted something to be super mean. I wanted to be hard to please. So, that when it did tell me I did a good job, I knew it. Like, it was good. And that's what this thing does.

**My kind of hack for this is I always instruct the AI, I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback.**

And then it's of course hilarious because it'll say now channeling my inner Bulshik, and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

## Open Source Alternative: OpenCode

Now, speaking of superpowers, let's talk about a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it.

You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called **OpenCode**.

```bash
# Install OpenCode
npm install -g opencode-cli
```

That was quick. And that's it. If I can just launch `opencode`. Just type it in like this.

Oh, we're here. This is OpenCode. A nice terminal user interface. Couple things real quick. They launched us straight into Grok Code fast one. They have a deal with Grok AI that allows you to use this for free for a while.

### Local Models Support

We can use local models. This is the killer part. I don't think any other tool does this, but we have to edit a file. So, I want to `nano` and I think it's inside `~/.config/opencode/opencode.json`.

I'm going to use let's do Llama 3.2. I think that's what I have installed. We'll find out. I'll save that.

And then when I launch OpenCode again with that config in place, I should be able to go `/model` and change to Llama 3.2. Hey, cool. Llama works.

If I back out, I can log into Claude with this command: `opencode login`. I can choose Anthropic with my Claude pro. And I'll

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-08 09:31:39

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,274,275
   - Comments: 4,240

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 440,384
   - Comments: 1,660

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 482,402
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 36,468
- Total Output Tokens: 20,198
- Total Tokens: 56,666
- **Total Cost: $0.4124**
- Model: Claude Sonnet 4


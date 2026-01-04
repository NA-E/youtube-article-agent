# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. Each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you.

You can use them for everything. And it's way better than their apps.

Writing, research, projects—working in the terminal is a superpower. I'm about to show you why. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Problem with Browser-Based AI

Tell me if this sounds like you because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

There's a better way to do this. Hear me out. It's in the terminal.

But before we dive into the terminal solutions, let's talk about why you're struggling with AI in the first place. You suck at prompting. It's okay. I did, too. But I got tired of asking AI to do things and getting garbage. Getting results like this when I'm expecting this. Like, have you ever yelled at ChatGPT? Like really insulted it? Because you're so frustrated with the results.

If you haven't, you're not using it enough. It's those moments, that frustration that makes me think one of two things. One, AI is dumb and I'm not going to use it anymore. Those naysayers are right. Or two, I'm dumb and I have no idea how to use AI. I most often feel like option two.

Here's the thing: if the AI model's response is bad, treat everything as like a personal skill issue. The problem is me. It's a skill issue. And I went deep to figure this out. I took all the top prompting courses on Coursera. I read all the official prompting docs, Anthropic, Google, OpenAI, and then I asked all the experts, the best prompt engineers I know.

## Understanding What Prompting Really Is

Most people, including me, get this fundamentally wrong. Prompting essentially is just asking AI to do stuff. And it almost feels like talking to a human. Sometimes we forget that it's not. But you have to remember you're talking to a computer.

A prompt is a call to action to the large language model. It's a call to action. But a prompt just isn't a question. It's a program. You aren't asking the AI. You're programming it with words. Every time we actually write something, ChatGPT needs to format it in a particular structure that we've given it. We've wrote a program that tells it what to do.

We need that mentality because LLMs don't think like we do. They are prediction engines. When you understand that an LLM is just super advanced autocomplete, that'll change your perspective. This response was statistically the best response according to it. But if we get more specific, you'll get way better results because you're hacking the probability.

You're not asking a question. You're starting a pattern. If your pattern is vague, the AI guesses anything. But if it's more focused, you'll get way better results.

## The Core Reality: AI Wants to Help (Maybe Too Much)

Here's something most people don't realize: AI is bad software but it's good people. A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said check back in a couple of days and I'll have it together. And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

Large language models have been instructed in certain ways to behave in certain ways. But you have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

The people who are the best users of AI are not coders, they're coaches. And so, if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

## Getting Started with Gemini CLI

We're diving straight into the terminal, and I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free.

### Installation

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux—all these terminal apps work everywhere. For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux.

```bash
# Installing Google Gemini CLI
curl -sSL https://get.gemini.com | bash

# For Mac users
brew install gemini-cli
```

If you run into a scary issue, run it with sudo. Now it's installed.

Before we launch it, we're going to make a new directory:
```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" It's doing a Google search right now. Pretty sick.

## The Terminal Advantage

Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: 99% context left. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

It's asking us a question. Do you want me to write a file for you? Do you want me to create a file for you? Yeah, dude. Go for it.

This thing can do everything a browser can do, but it has a superpower. **It can access your computer.** It can read and write files. Like, I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Feature: Context Files

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this.

Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files, and created instructions for itself—context for what we're working on.

Every time you launch Gemini, it's going to load that file as its context. Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

I'll tell it: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

I didn't give it any context. It just knew. This is a new chat session.

As I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project. I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just have this one file that helps keep us organized. Everything you need. You're never paralyzed again.

When I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

## The Meta Skill: Clarity of Thought

Here's what I learned from all the experts. There's one meta skill that is better than all the prompting techniques. It also is required for them all if you want to become a really good prompter. And that's clarity of thought.

Before he sits down to work on any kind of prompt or AI system, Daniel Mesler, one of the best prompt engineers I know, will sit down and describe exactly how he wants it to work. And he'll sit there and red team it, meaning he'll come at it from different angles and try to make sure it's robust. And he spends a lot of time in that upfront because if he does anything else, anything less than that, he'll end up getting frustrated and confused and it'll be a big mess.

If you can't explain it clearly yourself, you can't prompt it. And that's the key. That's the skill. I look back at my garbage prompts and they were messy because my thinking was messy.

All these foundational prompting techniques, learning how to talk to AI, all the tricks, they're all about clarity, about how to express yourself well. The persona forces you to say, who is answering this? Where's the source of knowledge coming from? What's the perspective? You have to think about that. Context forces us to say, "What are the facts? What does it need to know?"

The techniques aren't magic tricks, although you can try and use them that way, but eventually it's going to fail because you have to know how it's working, which boils down to how are you thinking? You have to get clear.

Using all these techniques doesn't make the AI smarter, although it feels like it is. All that's happening here is you got clearer. The AI can only be as clear as you are.

So, the next time you're getting frustrated with AI and you're tempted to yell at ChatGPT, look in the mirror. It's you. It's a skill issue. You're not explaining yourself. So, stop. Get a notebook out. Get a pen or just open up a blank note and try to describe what you want to do, what you're wanting to accomplish. Think first, prompt second.

## Essential Prompting Techniques for Terminal AI

Now that you understand the mindset, let's cover the essential techniques that will make your terminal AI experience incredible. These aren't magic tricks—they're about clarity and communication.

### 1. Context Engineering: Beyond Simple Prompts

Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

Context engineering is telling AI what you sound like. If you say, "Write me a sales email," it will. If you say, "Write me a sales email," in line with the voice and brand guidelines I've uploaded, it will write a totally different sales email. But that's just one part of the context.

You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add that also references our product specifications which were referenced in the call.

Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind. And for most people when we start working together, what they realize is they say, "Oh, I was kind of expecting AI to read my mind." All of the stuff that are implicit, you actually have to make explicit.

The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### 2. Personas: Give Your AI Personality

Who is writing your content when you ask AI to write it? Because generic responses sound like nobody. It's generic and soulless. That's where personas come in. We got to give this AI some personality.

Instead of just asking for help, try: "You're a senior site reliability engineer for Cloudflare. You're writing to both customers and engineers. Write an apology letter for the recent outage."

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just that prompt is saying I'd like you to be a professional communications expert. And if you have a favorite professional communications expert use them. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this? How do the principles that Dale Carnegie taught affect and influence and impact this correspondence?

When you're building outside of the GUI, for example, if you're using an API or Claude Code, you would normally have the persona in what's called the system prompt. When you're using a system like Claude Code, you can actually change that system prompt, which makes it super powerful.

### 3. Context: The Most Important Technique

Context literally takes the guesswork out of prompting almost. And 2025 has kind of been the year of context. Like context is king. You'll hear that.

This is the difference between writing, "give me some ideas for a birthday present under $30," and "give me five ideas for a birthday present. My budget is $30. The gift is for a 29-year-old who loves winter sports and has recently switched from snowboarding to skiing."

More context equals less hallucinations. Whatever context or information you don't include, it's going to fill in those gaps itself. They're eager to please. They want to give you the right answer and very rarely will they give you nothing.

**Pro tip:** Give your AI permission to fail. Tell it it's okay if it doesn't have an answer. Give it permission to say, "I don't know." You will explicitly say, "If it's not in the context, you can't find the answer, say, 'I don't know.'" If you don't say that, it will lie to please you. And this is the number one fix for hallucinations.

### 4. Chain of Thought Reasoning: Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. The weird thing about AI is it's true for AI too.

When you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model. So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step." That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you.

When you look at ChatGPT or Gemini or many others and you see the text scrolling, that's not some clever UX hack. That's not some cutesy design decision. That's literally how the model works. It's thinking one word at a time. But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word.

By asking a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer. By asking a model to think out loud, you know the answer to what are all of the assumptions that the model baked into its answer. And now you have the ability not only to evaluate the output, but also the thought process behind the output.

### 5. Few-Shot Examples: Show, Don't Tell

Few-shot prompting is another very important technique. The idea with few-shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that.

What if you gave the LLM examples of content you've already written exactly the way you want them, exactly the same tone and everything? That gives it much less room to guess and this gives you the best results.

The notion of few-shot prompting is effectively saying here's what a good output looks like to me. The idea is thinking for a moment, what is a quintessential example of the kind of output I want to receive. For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality or whatever it is? Why not include those emails in my prompt for an email?

Giving real examples is a much better approach than using adjectives. Somebody might say good example is easy but bad examples hard. It's only hard to the unaugmented person. If you have AI augmentation, which we now all do, you can say to an AI, I'm trying to few-shot prompt a model. I've got a good example, but I struggle even to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few-shot prompt?

Bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example.

### 6. Reverse Prompting: Let AI Ask Questions

The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt, "Help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

You basically give the model permission to ask you questions. This is part of the core of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. Any good manager would say that. But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

### 7. Output Requirements: Standardize Your Results

Telling the LLM exactly how you want the result to look is kind of a superpower. At the end of your prompts, give it clear output requirements:
- Clear bulleted list for timeline
- Keep it under 200 words
- The tone: professional, apologetic, radically transparent, no corporate fluff

## Claude Code: The Daily Driver

I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installing Claude Code

```bash
npm install -g claude-code
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

Again, don't be afraid. Ask Claude a question like, "I need to find a NAS for my house. Here's my budget, what I want to do. Create a report for me."

It responds similar to Gemini. And it can also have a context file, too. If I run that same command `/init`, it will create what's called a `claude.md` file. Noticing a trend here.

## The Power of Agents

Claude Code has a feature that changes the game: **Agents**. Look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

You can give it access to tools or restrict access. We'll give it everything. Choose our model. Sonnet's great. There's our agent. And we just made our first agent: Home Lab Guru.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'll give it this prompt and I'm calling the home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made.

It's going to use the home lab guru agent. There it is. There's our agent researching for us right now.

Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do." He's giving him a fresh set of instructions and get this, **a fresh context window**.

You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub-agents and never have to leave this conversation.

## Advanced Prompting Techniques

### Trees of Thought (ToT): Multiple Path Exploration

Where chain of thought explores one linear path, trees of thought explores multiple paths at once, like branches going on a tree. It's like going through a maze. Your goal is to get to the end, but you may have to follow a couple of different paths before you get there.

With problem solving, especially complex problems, the first idea isn't always best. So, it enables the AI to do self-correction. It generates a diversity of options.

Try this: "Brainstorm three distinct strategic approaches. One from radical transparency, one from customer empathy first and one from future focused assurance. Evaluate each branch. Synthesize them and then find the golden path."

One of the simplest techniques is trying on different constraints. One of the best ways you can solve a problem as a human is by forcing yourself to try on a bunch of different constraints. How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk? Anytime you make an association, you're colliding different information sources. The same is true for an AI.

### Battle of the Bots: Adversarial Validation

The community calls this one the playoff method. Researchers call it adversarial validation. I call it battle of the bots. Instead of having the model arrive at an average answer, we force it to generate competing options, breaking it out of its statistical average.

With this, we're generating a three round competition with three distinct personas. We got the engineer, the PR crisis manager, the angry customer. Round one, the engineer and the PR crisis manager write their own version. The angry customer reads both drafts and brutally critiques them. And then they read the customer's feedback and then collaborate to produce one final great result.

The reason this works is because AI is normally better at critiquing or editing than original writing. So, asking it to do this is actually tapping into its superpower.

## Preparing for Difficult Conversations with AI

If I'm going to use AI to roleplay a difficult conversation, I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Here's how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I'm going to go into the tough conversation personality profiler and say, "Hey, I'd love your help preparing for a conversation I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler gathers intelligence about the character and the scene. It asks questions about Jim's communication style, the context of the situation, and my desired outcome. Then it creates instructions for a separate AI to roleplay as Jim.

I open a new ChatGPT window and paste those instructions. Now I can practice the conversation with an AI version of Jim that behaves according to the personality profile. After the conversation, I can screenshot the transcript and get feedback from a third AI on how I performed, what I did well, and what I could improve.

You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback. It's a great way to basically get a flight simulator for a difficult conversation.

## Running Multiple AI Tools Simultaneously

I don't just use Claude Code. I use Gemini, I use Claude Code, and I use Codex which is ChatGPT's terminal tool all at the same time. Let me show you how.

Gemini, Claude Code, ChatGPT's Codex—I'm using all three right now to work on this video script. How? Two steps:

1. **Same Directory**: As long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

2. **Synced Context Files**: I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this:

- I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`.
- I'll have Gemini write a hook on a discovery angle. Write it to `discovery-hook.md`.
- Then I'll have Codex review it.

That's normally what I do. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work—the deep work. They're all using the same context, different roles. I mean, I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.

## Open Code: The Open Source Alternative

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called Open Code.

```bash
# Install Open Code
npm install -g opencode
```

You can open and close your terminal and launch it with just `opencode`.

They launched us straight into Grok code fast one. They have a deal with Grok AI that allows you to use this for free for a while. Same story.

The killer part? **We can use local models.** I don't think any other tool does this. You can switch models midway. Let's go back to Grok. What's our next step? While it's doing that, I can do new session. This is a new session. Push models to Claude.

You can also share these sessions. This is so crazy. The URL is copied to my clipboard. So, I can go to my browser, paste that URL in, and I can share your session with people. That's pretty neat.

We can do timeline. We can jump back in time and restore. I guess like if we don't like how far we've come in our conversation, we just go back. I want that in real life.

## The Real Power: Ownership

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project—it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive. I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.

And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. **I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

## My Daily Workflow

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex.

I rely on Claude to run my agent that will close out everything. So, I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent script session closer.

This is one of those agents I keep as a personal agent. I use it for many projects. And these agents are just files. They're files inside an agents folder.

Here's what the session closer does:
- It gathers everything we talked about, everything we did, and does a comprehensive summary
- It updates a session summary file that's specific to just updating what are some things that were done in the past sessions
- It sees if any core project files need to be updated
- If I'm talking with Claude, it will update every context file: Claude, Gemini, agents
- And then this is probably my favorite part: **I commit my project to a GitHub repo**

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So, I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. That's the power of using GitHub with all your ideas.

This is killer for me because I'm really bad at documentation. I'm really bad at keeping track of things, but now I have this help me keep track of things. So, when I'm really tired at the end of the day and like I've been working on a video and my mind is fried, I'm like, "Okay, tell you what, I'm done. Close this out." It will look through all this stuff. It will figure out where I'm at, end the project, end the day, where I need to be, and then I can start fresh the next day and be like, "Hey, um, where we at? What are we working on?" It can tell me, "Hey, Chuck, you finished the script. It's time to record. We made these three decisions. Go for it."

## The Critics: Making Me Better

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. So, here are my critics. These guys are so stinking mean. And I designe

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-04 09:23:03

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,248,434
   - Comments: 4,206

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 426,180
   - Comments: 1,618

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 479,896
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 35,259
- Total Output Tokens: 18,989
- Total Tokens: 54,248
- **Total Cost: $0.3906**
- Model: Claude Sonnet 4


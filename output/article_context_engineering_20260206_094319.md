# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: You can use them for everything. And it's way better than their apps.

Writing, research, projects – working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

But here's the thing – even if you switch to terminal AI tools, you'll still get garbage results if you don't know how to prompt properly. You suck at prompting. It's okay. I did, too. But I got tired of asking AI to do things and getting garbage. Getting results like this when I'm expecting this. Like, have you ever yelled at ChatGPT? Like really insulted it? Because you're so frustrated with the results.

## The Problem with Browser-Based AI

Tell me if this sounds like you, because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind.

You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works. At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

There's a better way to do this. Hear me out. It's in the terminal. But first, we need to fix your prompting. Because if the AI model's response is bad, treat everything as like a personal skill issue. The problem is me. It's a skill issue.

## Understanding What Prompting Really Is

Before we fix your prompting, you need to understand what prompting really is. And I know you think you know, but you actually don't know. Because most people, including me, get this fundamentally wrong.

Prompting essentially is just asking AI to do stuff. And it almost feels like talking to a human. Sometimes we forget that it's not. But you have to remember you're talking to a computer.

A prompt is a call to action to the large language model. It's a call to action. But a prompt just isn't a question. It's a program. You aren't asking the AI. You're programming it with words. Every time we actually write something, ChatGPT needs to format it in a particular structure that we've given it. We've wrote a program that tells it what to do.

We need that mentality because LLMs don't think like we do. They are prediction engines. When you understand that an LLM is just super advanced autocomplete, that'll change your perspective. This response was statistically the best response according to it. But if we get more specific, and I just mean a tiny bit specific, you'll get way better results because you're hacking the probability.

What I want to hit home is that you're not asking a question. You're starting a pattern. If your pattern is vague, the AI guesses anything. But if it's more focused, you'll get way better results because you're hacking the probability.

## The Evolution to Context Engineering

Now, what we've been talking about is really just the beginning. The real game-changer is something called context engineering. The first time I heard about it was when Andre Karpathy tweeted about it. I think probably Toby Lutke, the CEO of Shopify, also referenced it as well. I started digging into it. I mean, it's kind of an evolution of prompt engineering. Really, context engineering is just prompt engineering on steroids.

It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it? Here's a simple example: "Write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

Context engineering, one way to think about it is it's telling AI what you sound like. If you say, "Write me a sales email," it will. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add that also references our product specifications which were referenced in the call.

Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind. And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind." All of the stuff that are implicit, you actually have to make explicit.

The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## Getting Started with Gemini CLI

We're diving straight into the terminal, and I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free.

### Installation is Simple

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux – all these terminal apps work everywhere.

For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux. If you have no idea what that is, it's totally fine.

Installing Google Gemini CLI is straightforward:
```bash
# Standard installation
npm install -g @google/generative-ai-cli

# If you run into issues, use sudo
sudo npm install -g @google/generative-ai-cli

# On Mac, you can also use brew
brew install gemini-cli
```

### Setting Up Your Project

Before we launch it, we're going to make a new directory:
```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Terminal Superpower Revealed

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: "99% context left." Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

"I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources, and then compile the results into a document named best-coffee-method.md and then create me a blog plan, just an outline. I'll do the writing."

It's asking us a question: Do you want me to write a file for you? Yeah, dude. Go for it. This thing can do everything a browser can do, but it has a superpower. **It can access your computer. It can read and write files.**

I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer. Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

### The Context Revolution

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on.

Let's take a look at it: `cat gemini.md`. And while we didn't do much in this project, it knows what's going on. And every time you launch Gemini, it's going to load that file as its context.

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context, 100% left. Notice it's using our new gemini.md file. And I'll tell it this: "Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about. I didn't give it any context. It just knew. This is a new chat session.

## Mastering Prompting: The Foundation Techniques

Now, before we go deeper into terminal AI, let me show you how to prompt properly. Because even with these powerful tools, you'll get garbage if you don't understand the fundamentals.

### Personas: Give Your AI Personality

This sounds like nobody. It's generic and soulless. That's where personas come in. We got to give this AI some personality.

Who do we want crafting our email? Because guess what? AI can be anybody, also nobody. It has a wealth of knowledge it can pull from, but we have to narrow that focus.

Persona refers to what expertise you want the generative AI tool to draw from. We need to narrow its focus so it can guess better. Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus.

Very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet. You start to appreciate why simply giving a role helps because it starts to tell the AI where in your vast knowledge bank do I want you to draw information and make connections.

Let's try it out. "Hey, you're a senior site reliability engineer for Cloudflare." You're writing to both customers and engineers. Write an apology letter or email.

Boom. And immediately it's more professional from the subject line to the direct ownership. I'm instead of we. It's directed to a more technical audience. It's overall better.

### Context: The Most Important Technique

It's probably the most important technique I'm going to show you. It literally takes the guesswork out of prompting almost. And 2025 has kind of been the year of context. Like context is king.

This is the difference between writing, give me some ideas for a birthday present under $30, and give me five ideas for a birthday present. My budget is $30. The gift is for a 29-year-old who loves winter sports and has recently switched from snowboarding to skiing.

Whatever context or information you don't include, it's going to fill in those gaps itself. This is kind of the downside of LLM. They're eager to please. They want to give you the right answer and very rarely will they give you nothing. So more context equals less hallucinations.

My advice, never assume it knows something. Never assume it has all the context. Always provide all the context every time. ABC. Always be contexting.

Here's a trick I learned from Anthropic, their official prompting documentation. Give your AI permission to fail. Tell it it's okay if it doesn't have an answer. Give it permission to say, "I don't know." You will explicitly say, "If it's not in the context, you can't find the answer, say, 'I don't know.'" If you don't say that, it will lie to please you. And this is the number one fix for hallucinations.

### Output Requirements: Standardize Your Results

At the end of this, we're going to give it output requirements. Clear bulleted list for timeline. Keep it under 200 words. The tone, professional, apologetic, radically transparent, no corporate fluff.

Look at that. That's nice. Short, to the point. We're getting somewhere.

### Few-Shot Prompting: Show, Don't Tell

What if we gave the LLM examples of emails we've already written exactly the way we want them, exactly the same tone and everything? That gives it much less room to guess and this gives you the best results.

We can actually teach the large language model to follow a pattern using something called few-shot examples or few-shot prompting. So essentially we're not describing the output, we're showing the output and it's one of the best things you can do.

The idea with few-shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. And the notion of few-shot prompting is effectively saying here's what a good output looks like to me. The idea with few-shot prompting is thinking for a moment, what is quintessential example of the kind of output I want to receive.

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality or whatever it is? Why not include those emails in my prompt for an email? If you don't give any guidance, it's going to sound like whatever it thinks the average kind of response or the average output should sound like and most of the time its intuition is wrong.

Notice I'm not pasting the entire email or emails into this. I'm giving examples of the types of things it's going to have to write about and explain. So, here's what technical transparency looks like. Here's what a timeline looks like. Tone and ownership.

And then bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example. These giving real examples is a much better approach than using adjectives. Somebody might say good example is easy but bad examples hard. It's only hard to the unaugmented person. If you have AI augmentation, which we now all do, you can say to an AI, I'm trying to few-shot prompt a model. I've got a good example, but I struggle even to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few-shot prompt?

Doing this with any prompt you're about to use will make your experience with AI so much better.

## Claude Code: The Daily Driver

I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installing Claude Code

Let's get it installed with one command:
```bash
npm install -g @anthropic-ai/claude-code
```

And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

### The Agent Revolution

Now, I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**.

Look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10. And listen, that's just one of the seven features it has that keeps me glued to the terminal.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a "home lab research expert."

So, create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. You can always call them.

### Why Agents Are Game-Changing

Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."

He's giving him a fresh set of instructions and get this, **a fresh context window**. You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200k. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub-agents and never have to leave this conversation.

Claude just delegated this task to a new agent. He's got a fresh pot of coffee. He's ready to go. He just walked into work.

## Advanced Prompting Techniques

### Chain of Thought: Show Your Work

First, we have a little thing called CoT or chain of thought. It's showing your work. Just like a math class with chain of thought, we're telling the LLM to take steps to think step by step before it answers.

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. This is true for yourself. It's true if you're a parent working with a child. It's true if you're a manager working with a junior employee. Having someone just think out loud about how you would solve that problem often leads to a breakthrough. The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning.

Before writing this email, think through it step by step. This does two things for us. First, accuracy goes way up because it's actually thinking before it writes. Also, trust goes up because we're seeing what it's doing, how it came to its conclusions.

How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step." That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. So, if you say, for example, help me write this sales email. It doesn't say, what's a good sales email? Here it is. It's thinking one word at a time.

So, when you look at ChatGPT or Gemini or many others and you see kind of the text scrolling, that's not some clever UX hack. That's not some cutesy design decision. That's literally how the model works. It's thinking one word at a time. But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word.

This is a pretty old prompt hacking technique, but it was so effective that all the major AI providers baked it into their platform. Look at this. This little button right here, extended thinking. When I enable that, it automagically does just that.

All the major providers do it. You might see it called thinking or extended thinking. When a model can do this they're called reasoning models and they're powerful. From seeing how a lot of people use ChatGPT, 95% of all practical problems folks encounter can be solved by turning on extended thinking.

### Tree of Thought: Multiple Paths

This next one is incredibly fun. It's called ToT or trees of thought. So, where CoT explores one linear path, ToT explores multiple paths at once, like branches going on a tree.

With problem solving, especially complex problems, the first idea isn't always best. So, it enables the AI to do self-correction. It generates a diversity of options.

We're going to tell it to brainstorm three distinct tonal strategic approaches. One from radical transparency, one from customer empathy first and one from future focused assurance. Evaluate each branch. Synthesize them and then find the golden path.

### Battle of the Bots: Adversarial Validation

Let's get even crazier. The community calls this one the playoff method. Researchers call it adversarial validation. I call it battle of the bots. Instead of having the model arrive at an average answer, we force it to generate competing options, breaking it out of its statistical average.

With this, we're generating a three round competition with three distinct personas. We got the engineer, the PR crisis manager, the angry customer. Round one, the engineer and the PR crisis manager write their own version of the apology email. The angry customer reads both drafts and brutally critiques them. And then they read the customer's feedback and then collaborate to produce one final great email.

The reason this works is because AI is normally better at critiquing or editing than original writing. So, asking it to do this is actually tapping into its superpower.

### Reverse Prompting: Let AI Ask You Questions

Another technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt, you know, help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job. The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email." Well, can you tell me how much you sold of this skew in Q2 last year?

So, you basically give the model permission to ask you questions. This is part of the core actually of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. Right? Any good manager, imagine a manager who says, "Don't ask me any questions." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us human with questions unless we give it permission to ask them.

## Understanding AI's Personality: The Eager Intern Problem

Here's something crucial you need to understand: AI is bad software but it's good people. A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said check back in a couple of days and I'll have it together. And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

People hear from AI, "Check back in 15 minutes." If AI tells you that, it means it doesn't want to say, "I can't do it." Large language model has been instructed in certain ways to behave in certain ways. But you have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

The people who are the best users of AI are not coders, they're coaches. And so, if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

My kind of hack for this is I always instruct the AI, I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback. And then it's of course hilarious because it'll say now channeling my inner whatever, and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

When I realize that I'm dealing with a good person but a bad software, then it changes how I approach it and I ask for volume and I iterate and I ask it to try again and I ask it to reconsider.

## Advanced Roleplay: The Difficult Conversation Simulator

One of the most powerful applications is using AI to roleplay difficult conversations. I typically think about kind of three different chat windows, so to speak, one is a personality profiler. Two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Let me show you just how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I'm just going to go into the tough conversation personality profiler and I'm going to say, "Hey, I'd love your help preparing for a conversation I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler will gather intelligence about the character and the scene. It'll ask questions like: How would I describe Jim's communication style? What's the background of the situation? What's my best case outcome?

After I answer these questions, it gives me instructions to copy and paste into a new ChatGPT window that will create a realistic version of Jim for me to practice with. Then I can have the actual conversation, screenshot the transcript, and get feedback from a third AI on how I performed.

This is the first time in history I can get a flight simulator for a difficult conversation. You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback.

## Running Multiple AIs Simultaneously

Gemini, Claude Code, ChatGPT's CodeX – I'm using all three right now to work on this video script. How? Two steps:

1. **Same Directory**: As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project.

2. **Synced Context Files**: I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what CodeX uses, they're all the same.

Watch this. I'll tell Claude to write a hook for this video, authority angle, write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle, write it to `discovery-hook.md`, and then I'll have CodeX review it.

That's normally what I do. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work. I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.

## The Real Game Changer: Ownership

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project, it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive.

I can copy and paste that folder anywhere. All the work, all the decisions, all the context – **it's mine**.

That's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. I own my context. If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive.

I will use all AI. I will use the best AI. No one can stop me.

## My Daily Workflow System

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is CodeX.

I rely on Claude to run my agent that will close out everything. So, I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent: script session closer.

This is one of those agents I keep as a personal agent. I use it for many projects. And these agents are just files. They're files inside an agents folder.

### What My Session Closer Agent Does

Here's what this agent accomplishes:

- **Comprehensive Summary**: It gathers everything we talked about, everything we did, and creates a comprehensive summary
- **Updates Session History**: It updates a session summary file that's specific to just updating what things were done in past sessions
- **Core File Updates**: It checks if any core project files need to be updated
- **Context Sync**: If I'm talking with Claude, it will update every context file – Claude, Gemini, agents
- **Git Integration**: It commits my project to a GitHub repo

I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change, so I can see a history of why what I did and why I did it. Maybe something breaks, I can go back to that change and reinstate it. That's the power of using GitHub with all your ideas.

## The Brutal Critic System

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. I got the brutal critic. I told him to be mean. So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it."

I wanted something to be super mean. I wanted it to be hard to please. So that when it did tell me I did a good job, I knew it. Like, it was good.

While I've been talking with this AI for a minute, right? We've been going back and forth doing things. If I asked that session to review me, it would have a ton of bias coming into that based on what we've been talking about. I don't want that. I want a fresh cup of coffee critic coming in going, "Here's what I know NetworkChuck needs to have," and roast his current script on what he's doing.

## Open Source Alternative: OpenCode

There's a tool that's actually open source. Now, you can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick.

It's called OpenCode. We can install it with one command:
```bash
npm install -g @opencode/cli
```

### Local Models Support

The killer part is we can use local models. I don't think any other tool does this. You can edit a config file to use local models like Llama 3.2, or you can log into Claude with this command: `opencode login`.

You can choose Anthropic with your Claude Pro subscription, and now you're using Claude Code through OpenCode. All our files are local. Doesn't matter what tool we use. It's all ours right here. I can switch models midway.

What's fun is I've been following these guys on Twitter before they started making OpenCode. This guy Dax, these guys are killing it.

## The Meta Skill: Clarity of Thought

There's one meta skill that is better than them all. It also is required for them all if you want to become a really good prompter and learn how to really use AI.

I had an issue this week, actually. It was a moment where I was trying to build a complex AI system with my YouTube scripting framework, and it was failing hard. I got so frustrated. I was essentially yelling at Claude like I yell at ChatGPT. So I texted Daniel Mesler, one of the experts. He's a creator of Fabric, probably the best prompt engineer I know.

And he told me this. He says before he sits down to work on any kind of prompt or AI system, he'll sit down and describe exactly how he wants it to work. And he'll sit there and red team it, meaning he'll come at it from different angles and try to make sure it's robust. And he spends a lot of time in that upfront because if he does anything else, anything less than that, he'll end up getting frustrated and confused and it'll be a big mess, which is where I

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-02-06 09:43:19

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,468,735
   - Comments: 4,636

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 528,142
   - Comments: 1,884

3. [The 5 Step Playbook for 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 495,830
   - Comments: 483

**Cost Summary:**

- Total Input Tokens: 34,378
- Total Output Tokens: 18,105
- Total Tokens: 52,483
- **Total Cost: $0.3747**
- Model: Claude Sonnet 4


# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects – working in the terminal is a superpower. I'm about to show you why. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Problem We All Know Too Well

Tell me if this sounds like you because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. 

You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works. At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

**There's a better way to do this. Hear me out. It's in the terminal.**

But before we dive into the technical setup, let me share something crucial that will transform how you think about AI entirely. As Jeremy Utley from Stanford puts it: "AI is bad software but it's good people." Once you understand this fundamental truth, everything changes. **You're not dealing with a computer program – you're dealing with a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.**

## Getting Started with Gemini CLI (It's Free!)

We're diving straight into the terminal, and I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation is Dead Simple

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux – all these terminal apps work everywhere. For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux.

Copy and paste this command:
```bash
curl -sSL https://sdk.cloud.google.com | bash
```

Installing Google Gemini CLI. Ready, set, go. Coffee break while that goes. And if you run into a scary issue, run it with sudo just like this. And if you're on Mac, you can also use brew:
```bash
brew install gemini-cli
```

### Your First Terminal AI Experience

Now it's installed. Before we launch it, we're going to make a new directory:
```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?"

## The Terminal Superpowers Begin

Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

"I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

All right. Now, it's asking us a question. Do you want me to write a file for you? Do you want me to create a file for you? Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer. There they are.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Context Engineering Revolution

Here's where things get really powerful, and it connects to something Stanford's Jeremy Utley calls "context engineering." **Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?**

Think about it this way: if you say "write me a sales email," that's a prompt. ChatGPT will say, "Absolutely. Here's a compelling email," and they'll write it immediately. But what most people do is they say, "You know, it sounds like AI. It doesn't really sound like me." And what I often say is, have you told it what you sound like?

**If you say, "Write me a sales email," it will. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email.** But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer."

The simplest test for context engineering is actually the test of humanity. **Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.**

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files, and yes, go ahead, buddy. Create that file for me.

**What it just did there was create instructions for itself, context for what we're working on.** Let's take a look at it:
```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. And every time you launch Gemini, it's going to load that file as its context.

Let's test it. So, we still have our Gemini session open. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

"Write the intro for blog post one in the coffee series."

No more context. Just that. It should know exactly what I'm talking about. Look at that. **I didn't give it any context. It just knew. This is a new chat session.**

## Understanding the Architecture Behind Terminal AI

Now, here's what's actually happening under the hood that makes this so powerful. When you're working with these terminal AI tools, you're essentially building what's called an agent - think of it as a microservice. There's nothing particularly exotic about this, but it's fundamentally different from browser-based AI.

In technical terms, your terminal application becomes what's called the host application. It uses something like the MCP (Model Context Protocol) client library to create an instance of a client. Out there in the world, you have MCP servers that can be servers that already exist or servers you create yourself.

Inside these servers, you've got access to tools, resources, prompts, and capabilities that the server makes available and describes to the outside world. This is a server process with URLs, ports, and RESTful endpoints that tell the host application what tools are present, what sort of resources might be available, what prompts it has, and so on.

The connection between client and server can happen via standard IO for local processes, or through HTTP and Server Sent Events with JSON RPC messages. This setup allows for rich communication where servers can send asynchronous notifications back to the client.

## Claude Code: The Daily Driver

Now, I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**. Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys.

### Installing Claude Code

Let's get it installed with one command:
```bash
npm install -g @anthropic-ai/claude-code
```

And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of AI Agents

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

So, create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. You can always call them.

Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. **It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do."**

He's giving him a fresh set of instructions and get this, **a fresh context window**. You saw just now we have 200,000 tokens in our context window. We use 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Advanced Prompting Techniques That Actually Work

Now that you understand the power of terminal AI, let me share some advanced techniques that will make you exponentially more effective. These come from Stanford's research on AI collaboration, and they're game-changers.

### Chain of Thought Reasoning

One of the most powerful techniques is called chain of thought reasoning. **When you get an AI to think out loud, so to speak, you meaningfully improve the outputs of the model.** 

How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: **"Before you respond to my query, please walk me through your thought process step by step."**

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. **A language model does not premeditate a response to you.** It's thinking one word at a time.

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. **By asking a model to think out loud, you give the model the opportunity to bake all of its thought process about the task into its own answer.**

### Few Shot Prompting

**Few shot prompting is effectively saying here's what a good output looks like to me.** The idea is thinking for a moment, what is a quintessential example of the kind of output I want to receive?

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email?

**If you don't give any guidance, it's going to sound like whatever it thinks the average kind of response should sound like, and most of the time its intuition is wrong.**

Bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example. **Giving real examples is a much better approach than using adjectives.**

### Reverse Prompting

This technique is basically asking the model to ask you for the information it needs. **If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know?**

But if you reverse prompt the model and say at the end of your prompt: "Before you get started, ask me for any information you need to do a good job." The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email."

**You basically give the model permission to ask you questions.** If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

### Role Assignment

Assigning a role is one of the most foundational techniques because **it's effectively telling the AI where in its knowledge it should focus.** Very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just saying "please review this correspondence" is saying "I'd like you to be a professional communications expert." And if you have a favorite professional communications expert, use them. "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

## How Professional Agentic AI Really Works

Let me walk you through how this actually works in practice, because understanding this will change how you think about AI entirely. Let's say we're building a service for making appointments - meeting with somebody at some place, whether it's coffee, breakfast, or a romantic dinner.

Here's what happens behind the scenes: A prompt comes in like "I wanna have coffee with Peter next week." Your terminal application can interrogate the capabilities of connected servers and see what resources are available - calendar APIs, restaurant databases, location services.

The system asks the LLM: "Here is what my user said. Here is a list of resources. Do I need these?" The LLM responds with something like "Yes, you need resource two - that list of coffee shops in the area looks super interesting."

Your client then requests that specific resource, gets the data back, and provides it in the next prompt: "Here is my user prompt and here is the resource data. What should I do as a result?"

For tools, the foundation model APIs can actually receive structured data about available tools - the name, URL, parameter schema. In the reply, the LLM tells you "Yes, invoke this tool, pass these parameters." The AI doesn't actually call the tools (that would be a bit Skynet-y), but it gives you the recommendation, and your client code makes the decision.

## Running Multiple AIs Simultaneously

Gemini, Claude Code, ChatGPT's Codex. I'm using all three right now to work on this video script. How? Two steps:

1. **As long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context.** It's the same project.

2. **I make sure my context files are all synced up.** They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what Codex uses, and they're trying to make it a standard. They're all the same.

Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to `authority-hook.md`. I'll have Gemini write a hook on a discovery angle, write it to `discovery-hook.md` and then I'll have Codex review it.

**I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.**

## The Composability Revolution

Here's where it gets really interesting. These systems are composable. The server itself can be a client. Let's say you had some data source in Kafka out there, and you don't want to write a bunch of extra Kafka code. You can just use something like the Confluent MCP server and connect to that topic.

If you just need to consume from a Kafka topic, your server itself gets to be a client of another server. You've got pluggability, discoverability, composability - huge benefits that we want in professional code.

Instead of baking all functionality into one monolithic agent, you have components that are pluggable and discoverable. You don't need to know very much about what each tool does. You just plug it in, and the system goes through the process to discover and use its functionality.

## Taking Back Control of Your Data

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. **I own my context.**

If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

## My Daily Workflow System

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex.

I rely on Claude to run my agent that will close out everything. So, I'll just normally do this. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent script session closer.

**This is one of those agents I keep as a personal agent. I use it for many projects.** And these agents are just files. They're files inside an agents folder.

But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

**And then this is probably my favorite part. I commit my project to a GitHub repo.** So, normally you would use git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code.

## The Brutal Truth: AI Critics That Actually Help

I don't really use these AI terminal tools to help me create. **I use them to critique me and make me better.** So, here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean.

So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it." I wanted something to be super mean. I wanted to be hard to please. **So, that when it did tell me I did a good job, I knew it. Like, it was good.**

Here's my hack for this, straight from Stanford's playbook: **I always instruct the AI, I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback.**

And then it's of course hilarious because it'll say now channeling my inner bullshik, you know, it'll say something silly and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

**You have to know that all AI has been programmed to be a quote helpful assistant. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.**

## Practicing Difficult Conversations with AI

One of the most powerful applications I've discovered is using AI to practice difficult conversations. Here's how you can set up what I call a "flight simulator for difficult conversations."

I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver to get objective feedback on the conversation.

Let's say I need to have a conversation with my sales leader, Jim, about commission attribution. First, I go to my tough conversation personality profiler and describe the situation. It asks me questions like:
- How would I describe Jim's communication style?
- What's the backstory here?
- What's my best case outcome?

Then it generates instructions for creating a Jim character in a new ChatGPT window. I paste those instructions in, and now I have an AI playing Jim that I can practice with. After the conversation, I screenshot the transcript and upload it to my feedback agent, which grades my performance and gives me specific talking points for improvement.

**You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback. It's a great way to basically get a flight simulator for a difficult conversation.**

## Open Code: The Open Source Alternative

There's a tool that's actually open source. Now, you can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick.

It's called Open Code. We can install it with one command:
```bash
npm install -g open-code
```

**The killer part is we can use local models.** I don't think any other tool does this. You can also log into Claude with this command:
```bash
open-code login
```

I can choose Anthropic with my Claude Pro. And I can switch models midway. Let's go back to Grok. What's cool is I can do `/share` and watch this. This is so crazy. The URL is copied to my clipboard. So, I can go to my browser, paste that URL in, and I can share my session with people. That's pretty neat.

## The Coaching Mindset: Why This Actually Works

Here's the fundamental insight that changes everything: **The people who are the best users of AI are not coders, they're coaches.** They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

**If you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.**

Think about it this way: if you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me." Any good manager would say that. But imagine a manager who says, "Don't ask me any questions." That would be terrible management.

**But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.**

## Why This Changes Everything

So, how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

**I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone. Everyone should be using this.**

This really is a gateway to building true agentic AI in the enterprise, in a professional setting. There's a broader vision here than just enhancing a desktop application with some way to help you write code locally. When you understand the architecture - the pluggability, discoverability, and composability - you realize this is how professional AI applications should be built.

**Right now, the primary limitation is the limits of human imagination.** As Nobel Prize-winning economist Thomas Shelling said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

**If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.**

Nothing is stopping you from trying this right now. Gemini CLI, that's free. Open Code, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. Like, you saw all those features. I use that every day, dude.

**Just you got to try it. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower and build whatever you want.**

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

**Perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.**

I wake up every day feeling like I have superpowers. I want this for you.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-12-31 09:25:02

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,228,029
   - Comments: 4,180

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 635,316
   - Comments: 818

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 477,465
   - Comments: 475

**Cost Summary:**

- Total Input Tokens: 27,362
- Total Output Tokens: 13,890
- Total Tokens: 41,252
- **Total Cost: $0.2904**
- Model: Claude Sonnet 4


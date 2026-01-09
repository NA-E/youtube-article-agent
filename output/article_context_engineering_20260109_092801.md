# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects – working in the terminal is a superpower. I'm about to show you why. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

## The Browser Struggle Is Real

I know what you're thinking. "Chuck, I use AI just fine." Do you? Tell me if this sounds like you, because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. **There's a better way to do this. Hear me out. It's in the terminal.**

But here's the deeper issue that most people don't realize: **AI is bad software but it's good people.** When you understand this fundamental truth, it changes everything about how you approach AI collaboration. The AI wants to be helpful, it's predisposed to say yes, and it's like a super eager, super enthusiastic intern who's tireless and capable but not really great at pushing back or setting boundaries.

## The Architecture Revolution: How Terminal AI Actually Works

Before we dive into the tools, let's understand what's happening under the hood. When you use AI in the browser, you're basically stuck with this: you have a prompt, you send it to an LLM, and you get a response back. That response is just words. If words are what you want, you're doing fine. But what if you want to do something? What if you want to cause effects out in the world?

**That's what agentic AI is all about.** The AI needs to be able to take actions, invoke tools, and access up-to-date information that's not available in the core foundation model. This could be files, databases, real-time data streams, or any resources in your world that the agent needs to be aware of.

The terminal changes everything because it breaks your AI out of that browser prison. Instead of being limited to just generating text, your AI can now access your computer, read and write files, run scripts, and integrate with external systems through what's called the Model Context Protocol (MCP).

Think of it like this: you're building an agent – essentially a microservice. In MCP terms, this is called the host application. The host uses an MCP client library to connect to MCP servers that provide tools, resources, prompts, and capabilities. **It's pluggable, discoverable, and composable – huge benefits that we want in our code.**

## The Context Engineering Revolution

Here's where things get really powerful. Most people think they're doing prompt engineering, but what they're really missing is **context engineering**. The first time I heard about it was when Andre Karpathy tweeted about it, and it's basically prompt engineering on steroids.

Context engineering is asking: what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for? Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, "Absolutely. Here's a compelling email," and they'll write it immediately. 

But what a lot of people do is they say, "It sounds like AI. It doesn't really sound like me." And what I often say is, **have you told it what you sound like?** Most people go, "Oh no, I haven't."

If you say "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer" and then add "that also references our product specifications which were referenced in the call."

**Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind.** All of the stuff that are implicit, you actually have to make explicit. The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## Getting Started with Gemini CLI (It's Free!)

We're diving straight into the terminal. And I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like. I want you to try it so you can know it's not really scary. The terminal is a fun place.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation is Simple

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux – all these terminal apps work everywhere. For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux.

```bash
# Install Gemini CLI
curl -sSL https://storage.googleapis.com/gemini-cli/install.sh | bash

# Or on Mac with Homebrew
brew install gemini-cli
```

If you run into a scary issue, run it with sudo. Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Terminal Superpowers Begin

Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" Notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources, and then compile the results into a document named best-coffee-method.md and then create me a blog plan – just an outline. I'll do the writing."

It's asking us a question: "Do you want me to write a file for you?" Yeah, dude. Go for it.

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. Look, it actually made files on our computer. There they are: best-coffee-method.md, coffee-blog.md.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a gemini.md file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on.

Let's take a look at it:

```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. **And every time you launch Gemini, it's going to load that file as its context.**

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context, 100% left. Notice it's using our new gemini.md file. And I'll tell it this: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

Look at that. I didn't give it any context. It just knew. This is a new chat session.

## Advanced Techniques: Chain of Thought Reasoning

Here's something that will dramatically improve your AI outputs: **chain of thought reasoning**. Cognitive scientists have known for a long time that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves.

The weird thing about AI is it's true for AI too. When you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model. So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it.

**Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step."** That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. When you look at ChatGPT or Gemini and you see the text scrolling, that's not some clever UX hack. **That's literally how the model works. It's thinking one word at a time.**

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. So when you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

## Claude Code: The Daily Driver

Now, I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**. Like, look at this. I have seven agents performing tasks right now in one terminal. Actually, there's 10.

Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installing Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Then launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of Agents

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a "home lab research expert."

So create a new agent. Notice it'll ask us where do you want to make it? Because you can have agents that are tied to just this project we're working on or personal agents that are tied to everything. We'll do just this project.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this.

I'm going to give it this prompt and I'm calling the home lab agent. It'll figure it out. I'll have it create a document and I'll say make sure you reference the research we made.

**It's going to use the home lab guru agent. Claude was like, "Cool, I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers."** And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do." He's giving him a fresh set of instructions and get this, **a fresh context window**.

You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub-agents and never have to leave this conversation.

## Advanced Prompting Techniques

### Few Shot Prompting: Teaching by Example

Few shot prompting is another very important technique. The idea with few shot prompting is an **AI is an exceptional imitation engine**. If you don't give an example, it imitates the internet, but it doesn't do much more than that.

The notion of few shot prompting is effectively saying here's what a good output looks like to me. Think for a moment, what is a quintessential example of the kind of output I want to receive? For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email?

**Giving real examples is a much better approach than using adjectives.** If you don't give any guidance, it's going to sound like whatever it thinks the average response should sound like, and most of the time its intuition is wrong.

Bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example. And if you struggle with bad examples, you can ask an AI: "I'm trying to few shot prompt a model. I've got a good example, but I struggle to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few shot prompt?"

### Reverse Prompting: Let AI Ask the Questions

Another technique that I think is table stakes for collaborating well with AI is something called **reverse prompting**, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating. You go, "Where did it get these sales numbers?" Well, here's my question: Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt: "Help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

**You basically give the model permission to ask you questions.** This is part of the core of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

### Role Assignment: Focusing the AI's Knowledge

**Assigning a role is one of the most foundational techniques** that you can leverage because it's effectively telling the AI where in its knowledge it should focus. Very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just "please review this correspondence" is saying "I'd like you to be a professional communications expert." And if you have a favorite professional communications expert, use them. "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this? How do the principles that Dale Carnegie taught affect and influence and impact this correspondence?"

## Running Multiple AIs Simultaneously

Here's the craziest part about this. Everything I'm doing, talking with these three different AIs on a project – Claude, Gemini, and CodeX (ChatGPT's terminal tool) – it's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. **I own my context.**

If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

### How I Keep Everything Synced

As long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project. The second thing I do is I make sure my context files are all synced up. They all say the same thing. So gemini.md, claude.md, and agents.md, which is what CodeX uses – they're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this:

- I'll tell Claude to write a hook for this video, authority angle, write it to authority-hook.md
- I'll have Gemini write a hook on a discovery angle, write it to discovery-hook.md  
- Then I'll have CodeX review it

That's normally what I do. I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work. **I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.**

## Understanding the MCP Workflow

Let me walk you through exactly how this magic happens under the hood. Let's say you're building a service for making appointments – maybe getting coffee, breakfast, or dinner with someone. You need calendar integration, restaurant reservations, knowledge of local venues. Instead of baking all that functionality directly into your agent, you put it in an MCP server.

Here's the workflow: A prompt comes in like "I wanna have coffee with Peter next week." Your host application asks the MCP server, "What capabilities do you have?" It gets back a list of resources with text descriptions. Then you ask your LLM: "Here is what my user said. Here is a list of resources. Do I need these?"

The LLM tells you, "Yes, you need resource two – that list of coffee shops in the area looks super interesting." So your client goes and asks the MCP server for the details of resource two, gets that data back, and includes it in the next prompt: "Here is my user prompt. And now here is the resource data. What should I do as a result?"

**The beauty is in the discoverability.** You don't need to know very much about what each tool does. You just plug it in, and the system figures out how to use it through this standardized protocol.

## Advanced AI Collaboration: Roleplay Training

Here's a technique that will revolutionize how you prepare for difficult conversations. You can use AI to roleplay any challenging situation using a three-window approach: a personality profiler, the character of the individual you need to speak to, and a feedback giver for objective evaluation.

Let's say I need to have a difficult conversation with my sales leader, Jim, about commission attribution. I start with the personality profiler and give it background: "I need to prepare for a conversation with my sales leader, Jim. He emailed me saying he deserves commission on a deal that I know came through a different channel."

The profiler asks me questions about Jim's communication style, the context of the situation, and my desired outcome. I tell it Jim is direct, confrontational, typical East Coaster, sarcastic. The deal came through our social team's LinkedIn campaign, and I want Jim to back down and agree that social team gets the commission.

Then I copy the profiler's instructions into a new ChatGPT window to create "Jim." I start the roleplay: "Hey, Jim. Do you have a second?" And Jim responds in character. After the conversation, I take screenshots and upload them to a feedback GPT that evaluates my performance and gives me a grade with specific improvement suggestions.

**This is the first time in history I can get feedback before having the real conversation.** You can use this for any difficult conversation, whether it's a performance review, salary negotiation, or difficult feedback. It's like having a flight simulator for difficult conversations.

## The Brutal Critics

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. So here are my critics. These guys are so stinking mean. And I designed them to be.

I got the brutal critic. I told him to be mean. So I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it." I wanted something to be super mean. I wanted it to be hard to please. **So that when it did tell me I did a good job, I knew it. Like, it was good.**

Here's my hack for this: I always instruct the AI, "I want you to do your best impression of a Cold War era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

**AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.** But when you explicitly ask for brutal honesty, you get insights that actually help you improve.

What I love about this is while I've been talking with this AI for a minute, if I asked that session to review me, it would have a ton of bias coming into that based on what we've been talking about. I don't want that. **I want a fresh cup of coffee critic coming in going, "Here's what I know NetworkChuck needs to have," and I'm going to roast his current script.**

## My Daily Workflow System

This video was made with this process. I rely on Claude to run my agent that will close out everything. So I'll just normally do this when I'm done for the day: "Hey, let's close this out." Run my script session closer agent.

This agent does a lot of stuff, but some key things:
- It gathers everything we talked about, everything we did, and does a comprehensive summary
- It updates a session summary file specific to just updating what are some things that were done in past sessions
- It sees if any core project files need to be updated
- If I'm talking with Claude, it will update every context file: Claude, Gemini, agents
- **And then this is probably my favorite part: I commit my project to a GitHub repo**

Normally you would use Git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change, so I can see a history of why what I did and why I did it.

**That's the power of using GitHub with all your ideas.**

## Open Code: The Open Source Alternative

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called Open Code:

```bash
# Install Open Code
curl -sSL https://opencode.dev/install.sh | bash
```

A couple things real quick. They launched us straight into Grok Code Fast One. They have a deal with Grok AI that allows you to use this for free for a while. **The killer part is we can use local models. I don't think any other tool does this.**

You can log into Claude with this command:

```bash
opencode login
```

You can choose Anthropic with your Claude Pro, and now I'm logged into Claude Code. **I can switch models midway.** All our files are local. Doesn't matter what tool we use. It's all ours right here.

## The Enterprise Vision: Building Professional Agentic AI

Here's where this gets really exciting. What we're talking about isn't just enhancing desktop applications with some agentic functionality. **This is really a gateway to building true agentic AI in the enterprise, in a professional setting.**

The MCP architecture gives you pluggability, discoverability, and composability. These servers can even be clients of other servers. Say you have data in Kafka that you need to access – you don't need to write a bunch of Kafka code. You can just use an existing Confluent MCP server and connect to that topic.

**This composable architecture means you can build sophisticated AI workflows that integrate with all your existing enterprise systems.** Your AI agents can access databases, message queues, APIs, file systems – anything you need to get real work done.

## The Coaching Mindset: The Secret to AI Mastery

Here's the key insight that will transform your AI collaboration: **The people who are the best users of AI are not coders, they're coaches.** They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

If you aren't careful, AI will gaslight you. Remember, AI has been programmed to be a helpful assistant. It's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless and capable but not really great at pushing back or setting boundaries.

**When I realize that I'm dealing with good people but bad software, then it changes how I approach it.** I ask for volume and I iterate and I ask it to try again and I ask it to reconsider. The good news is if you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

## Expanding Human Imagination

Where could AI go? Well, it's really a function of who can get unleashed. Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally.

One of my favorite quotes is from Nobel Prize-winning economist Thomas Schelling. He said, **"No matter how heroic a man's imagination, he could never think of that which would not occur to him."** If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

This has been called the adjacent possible in innovation studies for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible.

## Why This Changes Everything

So how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. **Break out of that browser, that chat window, and don't let the terminal scare you.**

I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone. Everyone should be using this. **Nothing is stopping you from trying this right now.**

- Gemini CLI: that's free
- Open Code: you can run local models if you're worried about that
- And while Claude Code is paid, it's overpowered

**You will feel like you have a superpower and build whatever you want.**

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. **What can you build for you that's just for you and your niche and whatever you're trying to make happen?**

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

**And perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.** Seriously, nothing is stopping you from trying this right now. Dip your toe in the water. It's fine. It's awesome. **You will feel like you have a superpower.**

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-09 09:28:01

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,280,796
   - Comments: 4,261

2. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 639,273
   - Comments: 821

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 483,029
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 27,584
- Total Output Tokens: 14,739
- Total Tokens: 42,323
- **Total Cost: $0.3038**
- Model: Claude Sonnet 4


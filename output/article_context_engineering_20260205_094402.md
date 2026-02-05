# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: **You can use them for everything. And it's way better than their apps.**

Writing, research, projects - working in the terminal is a superpower. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

But before we dive into these game-changing tools, we need to talk about something crucial: **You probably suck at prompting.** I did too. And if you're getting garbage results from AI, it's not the AI's fault - it's a skill issue. The problem is you.

## The Browser Problem We All Know Too Well

Chuck, I use AI just fine. Do you? Tell me if this sounds like you because this is how I used to use AI:

You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes.

**There's a better way to do this. Hear me out. It's in the terminal.**

## Understanding What AI Really Is (The Foundation You Need)

Before we fix your prompting and show you these terminal superpowers, you need to understand what prompting really is. And I know you think you know, but you actually don't know. Because most people, including me, get this fundamentally wrong.

Prompting essentially is just asking AI to do stuff. And it almost feels like talking to a human. Sometimes we forget that it's not. But you have to remember you're talking to a computer.

**You aren't asking the AI. You're programming it with words.** Every time we write something, ChatGPT needs to format it in a particular structure that we've given it. We've wrote a program that tells it what to do. We need that mentality because LLMs don't think like we do. They are prediction engines.

When you understand that an LLM is just super advanced autocomplete, that'll change your perspective. They're not thinking about your request - they're completing it based on patterns they've seen. This response was statistically the best response according to it. But if we get more specific, we can hack the probability and get way better results.

Here's the crucial part most people miss: **AI is bad software but it's good people.** It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. They're not really great at setting boundaries. And so if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

## The Four Pillars of Better Prompting

### 1. Personas: Give Your AI Personality

This Cloudflare apology email is kind of trash. And I think it has to do with who is writing this. Who is writing this email when we ask AI to write it? It sounds like nobody. It's generic and soulless.

That's where personas come in. We got to give this AI some personality. Instead of asking it to write generically, try: "Hey, you're a senior site reliability engineer for Cloudflare. You're writing to both customers and engineers. Write an apology letter."

**AI can be anybody, also nobody.** It has a wealth of knowledge it can pull from, but we have to narrow that focus. Persona refers to what expertise you want the generative AI tool to draw from. It helps narrow its focus so it can guess better.

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. So very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

### 2. Context: The Most Important Technique

It's probably the most important technique I'm going to show you. It literally takes the guesswork out of prompting almost. **More context equals less hallucinations.**

This is the difference between writing "give me some ideas for a birthday present under $30" and "give me five ideas for a birthday present. My budget is $30. The gift is for a 29-year-old who loves winter sports and has recently switched from snowboarding to skiing."

Whatever context or information you don't include, it's going to fill in those gaps itself. They're eager to please. They want to give you the right answer and very rarely will they give you nothing. 

**ABC. Always be contexting.** Never assume it knows something. Never assume it has all the context. Always provide all the context every time. And here's a crucial trick: **Give your AI permission to fail.** Tell it it's okay if it doesn't have an answer. You will explicitly say, "If it's not in the context, you can't find the answer, say 'I don't know.'" If you don't say that, it will lie to please you. This is the number one fix for hallucinations.

Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it? All of the stuff that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### 3. Output Requirements: Standardize Your Results

Telling the LLM exactly how you want the result to look is kind of a superpower. At the end of your prompt, give it output requirements: "Clear bulleted list for timeline. Keep it under 200 words. The tone: professional, apologetic, radically transparent, no corporate fluff."

### 4. Few-Shot Examples: Show, Don't Tell

What if we gave the LLM examples of exactly what we want? We can actually teach the large language model to follow a pattern using something called few-shot examples or few-shot prompting. Essentially we're not describing the output, we're showing the output and it's one of the best things you can do.

Don't paste entire examples - give focused snippets that show the types of things it needs to write about. This makes it very clear and gives it much less room to guess.

Few-shot prompting is another very important foundational technique. The idea is that AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. The notion of few-shot prompting is effectively saying here's what a good output looks like to me.

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email? And bonus points if you actually give a bad example. These giving real examples is a much better approach than using adjectives.

## Advanced Prompting Techniques That Change Everything

### Chain of Thought: Making AI Think Step by Step

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. The weird thing about AI is it's true for AI too.

Chain of thought is about showing your work. Just like a math class, we're telling the LLM to take steps to think step by step before it answers. It looks like this: "Before writing this email, think through it step by step."

This does two things for us. First, accuracy goes way up because it's actually thinking before it writes. Also, trust goes up because we're seeing what it's doing, how it came to its conclusions.

How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step."

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. When you look at ChatGPT or Gemini and you see the text scrolling, that's not some clever UX hack. That's literally how the model works. It's thinking one word at a time.

When you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

### Trees of Thought: Exploring Multiple Paths

Where chain of thought explores one linear path, trees of thought explores multiple paths at once, like branches on a tree. It's like going through a maze - you may have to follow a couple of different paths before you get to the end.

Try this: "Brainstorm three distinct tonal strategic approaches. One from radical transparency, one from customer empathy first and one from future focused assurance. Evaluate each branch. Synthesize them and then find the golden path."

It enables the AI to do self-correction. It can go down one path and go, "Oh, dead end." Go down this path. "Oh, that's a good one." It generates a diversity of options.

### Battle of the Bots: Adversarial Validation

The community calls this one the playoff method. Researchers call it adversarial validation. I call it battle of the bots. Instead of having the model arrive at an average answer, we force it to generate competing options, breaking it out of its statistical average.

Generate a three-round competition with three distinct personas. Have them compete, critique each other, then collaborate on a final result. AI is normally better at critiquing or editing than original writing. So asking it to do this is actually tapping into its superpower.

### Reverse Prompting: Let AI Ask You Questions

One technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know?

But if you reverse prompt the model and say at the end of your prompt: "Help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

You basically give the model permission to ask you questions. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

## Getting Started with Gemini CLI: Your First Taste of Terminal AI

Now that you understand how to prompt properly, let's dive straight into the terminal. I know you probably have some questions. Put those in your pocket for a second. We'll address those. But I first just want to show you what it looks like.

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, **free**.

### Installation and Setup

We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux - all these terminal apps work everywhere.

```bash
# Installing Google Gemini CLI
curl -sSL https://storage.googleapis.com/gemini-cli/install.sh | bash

# If you run into issues, use sudo
sudo curl -sSL https://storage.googleapis.com/gemini-cli/install.sh | bash

# On Mac, you can also use brew
brew install gemini-cli
```

Now it's installed. Before we launch it, we're going to make a new directory:

```bash
mkdir coffee-project
cd coffee-project
```

Now we can launch Gemini. You'll see why I did this here in a second. Type in `gemini`. One word. Ready, set, go.

First, isn't that logo just awesome? I love the terminal. It's so nostalgic. Now, first thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account.

## The Superpower Difference

Don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?"

That wasn't so bad, was it? But notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: **99% context left**. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> "I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing."

**This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files.** Like, I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changing Context Feature

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that. Go.

What it's doing right now is something powerful. It's creating a `gemini.md` file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on.

Let's take a look at it:

```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. **And every time you launch Gemini, it's going to load that file as its context.**

Let's test it. So, we still have our Gemini session open. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new `gemini.md` file.

And I'll tell it this: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

I didn't give it any context. It just knew. This is a new chat session. **No reexplaining the context, no starting over, no more 20 scattered chats.** We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

## Claude Code: The Daily Driver

Now, when I saw this, I'm like, this is it. I finally have control over my context, my files, my projects. They're not stuck in some browser chat session anymore. They're right here, sitting on my hard drive. Mine, my precious.

But I don't just use Gemini. It's not even close to the best one. Let's look at Claude Code, my daily driver. This one's so crazy.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

### Installing Claude Code

```bash
npm install -g @anthropic-ai/claude-dev
```

And then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. That's it. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Revolutionary Agent System

Now, I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: **Agents**. Like, look at this. I have seven agents performing tasks right now in one terminal.

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. Just like this. We'll get a terminal menu and let's create a home lab research expert.

**So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers."** And this is another Claude instance. It's like a guy sitting over there. He's like, "Hey buddy, are you busy? Here's some work to do." He's giving him a fresh set of instructions and get this, a fresh context window.

You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Running Multiple AI Systems Simultaneously

Let's get crazier. I'll create another tab because no one can stop us. Jump into our project. Launch Claude in dangerous mode. And what do you say we have Claude use Gemini for research? Yes, because we can run Gemini and Claude and all these terminal tools in headless mode, meaning you don't jump into a TUI. You just run them with one command.

It's like `gemini -p "Find pizza"`. We can just create an agent that does that.

**We're having an AI use an AI right now.**

## The Multi-AI Workflow

Gemini, Claude Code, ChatGPT's CodeX. I'm using all three right now to work on this video script. How? Two steps.

First, as long as I open up Claude, Gemini, and CodeX in the same directory, they're all using the same context. It's the same project.

The second thing I do is I make sure my context files are all synced up. They all say the same thing. So `gemini.md`, `claude.md`, and `agents.md`, which is what CodeX uses, and they're trying to make it a standard. They're all the same.

**I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.**

## Taking Back Control of Your AI Workflow

Now, are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project. It's not tied in a browser. It's not tied in a GUI. **It's just this folder right here on my hard drive.**

I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine. And that's the difference.

Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock in so I can't leave. No, I reject that. **I own my context.** If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

## My Daily Workflow System

This video was made with this process. When I'm done for the day, I'll go, "Hey, let's close this out." And I'll mention my agent script session closer. This is one of those agents I keep as a personal agent. I use it for many projects.

But first, it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file that's specific to just updating what are some things that were done in the past sessions. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

And then this is probably my favorite part. **I commit my project to a GitHub repo.** So, normally you would use git for code, right? For writing and deploying code. I treat my scripts and pretty much every project I work on in my life like code.

## The Brutal Critic System

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. So, here are my critics. These guys are so stinking mean. And I designed them to be. They are agents. I got the brutal critic. I told him to be mean.

So, I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it." I wanted something to be super mean. I wanted to be hard to please. So, that when it did tell me I did a good job, I knew it. Like, it was good.

My kind of hack for this is I always instruct the AI: "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback." And then it's of course hilarious because it'll say now channeling my inner Bolshoi, you know, it'll say something silly and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

## Advanced Roleplay and Simulation

You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, difficult feedback. It's a great way to basically get a flight simulator for a difficult conversation.

If I'm going to use AI to roleplay a difficult conversation, I typically think about kind of three different chat windows, so to speak: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Here's how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I'll go into the tough conversation personality profiler and say, "Hey, I'd love your help preparing for a conversation. I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler will gather intelligence about the character and the scene, asking questions like: How would I describe Jim's communication style? What's the best case outcome of this conversation?

Then I take those instructions and paste them into a new ChatGPT window to create the Jim character. After having the practice conversation, I can screenshot the transcript and get feedback from a third AI about what I did well and what I could improve.

The point is historically the only time I get feedback is after I have the real conversation with Jim. This is the first time in history where I can get a flight simulator for a difficult conversation that prepares me in context for this specific situation.

## OpenCode: The Open Source Alternative

There's a tool that's actually open source. Now, you can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

Let's play with it. It's called OpenCode.

```bash
# Install OpenCode
npm install -g opencode-cli
```

This is OpenCode. A nice terminal user interface. They launched us straight into Grok Code fast one. They have a deal with Grok AI that allows you to use this for free for a while.

We can use local models. This is the killer part. I don't think any other tool does this, but we have to edit a file.

```bash
nano ~/.config/opencode/opencode.json
```

**I can switch models midway.** I guess again all our files are local. Doesn't matter what tool we use. It's all ours right here.

## The Meta Skill That Changes Everything

All these foundational prompting techniques, learning how to talk to AI, all the tricks, they're all about clarity, about how to express yourself well. The persona forces you to say, who is answering this? Context forces us to say, "What are the facts? What does it need to know?" Chain of thought forces us to think about how the logic will flow.

**The techniques we're seeing here aren't magic tricks. All that's happening here is you got clearer.**

If the AI model's response is bad, treat everything as like a personal skill issue. The problem is you. You didn't explain it well enough or you didn't give it enough context. The more specific you could get, the better results you'll get.

**That's the meta skill. Clarity of thought.** When you're struggling with AI, it's not the AI's fault. It's not a prompting problem. It's that you don't really yet know how to think clearly. The AI can only be as clear as you are.

So, the next time you're getting frustrated with AI and you're tempted to yell at ChatGPT, look in the mirror. It's you. It's a skill issue. You're not explaining yourself. So, stop. Get a notebook out. Get a pen or just open up a blank note and try to describe what you want to do, what you're wanting to accomplish. **Think first, prompt second.**

And that's kind of what I love about AI. If you're really trying to get good at AI, the way you think, the way you have to design and think about systems and view the world, that ability is going to increase if you embrace this. And that's the superpower. That's the skill right now to learn - knowing how to describe a system and describe a problem.

## AI as Mirror: Preserving Your Critical Thinking

Some people are concerned about cognitive offloading - this observed phenomenon that humans actually kind of stop thinking or as one researcher put it, fall asleep at the wheel. People are concerned right now: is AI just making us dumber?

My feeling is AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

For example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

## Building Your Prompt Library

Once you figure out that good prompt, save that sucker. Get a prompt library. You can use a prompt enhancer prompt to enhance your prompts for better prompts. But before I do that, I always make sure my ideas are clear and what I'm describing makes sense to me. I try to imagine like if I were to hand this to a human and say, "Is this enough information for you to do this thing?" Then I know an AI can probably do it, too.

## The Expanding Adjacent Possible

One of my favorite quotes is from Nobel Prize-winning economist Thomas Schelling. He said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands. In innovation studies, this has been called the adjacent possible for a long time. What is possible is just adjacent to what is.

As we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible. Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally.

## Why This Changes Everything

So, how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel because now you can control your context. Break out of that browser, that chat window, and don't let the terminal scare you.

I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, **this tool is for everyone. Everyone should be using this.**

Seriously, nothing is stopping you from trying this right now. Gemini CLI, that's free. OpenCode, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. Like, you saw all those features. I use that every day, dude.

**Leaving the browser, going to your terminal, puts you back in control, and it gives you better features.** You own your context. You control your workflow. And when the next great AI comes along, you'll be ready for it because everything you've built, all your work, all your context - it's yours, sitting right there on your hard drive.

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you. **You will feel like you have a superpower and build whatever you want.**

Perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind. The adjacent possible is waiting for you to explore it.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-02-05 09:44:02

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,461,831
   - Comments: 4,630

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 525,103
   - Comments: 1,871

3. [The 5 Step Playbook for 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 495,350
   - Comments: 485

**Cost Summary:**

- Total Input Tokens: 33,788
- Total Output Tokens: 16,813
- Total Tokens: 50,601
- **Total Cost: $0.3536**
- Model: Claude Sonnet 4


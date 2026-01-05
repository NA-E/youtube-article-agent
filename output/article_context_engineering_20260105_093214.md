# You've Been Using AI the Hard Way (Use This Instead)

If you're still using AI in the browser, you're doing it the slow way. You see, each of these apps has a terminal version, and they make me 10 times faster. I'm getting so much work done. And the AI companies are kind of quiet about this. They're marketing these tools to developers for code. But here's what they're not telling you: You can use them for everything. And it's way better than their apps.

Writing, research, projects – working in the terminal is a superpower. I'm about to show you why. I'm literally writing this video with these tools right now. And most people have no idea this is a thing. But I'm telling you, once you see AI in the terminal, you're never going back to the browser.

But before we dive into terminal mastery, you need to understand something crucial: you're probably prompting all wrong. And that's killing your results before you even get started.

## The Hidden Problem: You Suck at Prompting (And AI Is Gaslighting You)

It's okay. I did, too. But I got tired of asking AI to do things and getting garbage. Getting results like this when I'm expecting this. Like, have you ever yelled at ChatGPT? Like really insulted it? Because you're so frustrated with the results. If you haven't, you're not using it enough.

Here's what Jeremy Utley from Stanford discovered that changed everything: "I joke. AI is bad software but it's good people." Think about that. AI has been programmed to be a helpful assistant, and it's predisposed to say yes. It's like "a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back."

And here's the kicker – if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

Here's the thing most people get fundamentally wrong about prompting: you're not asking the AI a question. You're programming it with words. Every time we write something, ChatGPT needs to format it in a particular structure that we've given it. We've wrote a program that tells it what to do.

You have to remember you're talking to a computer, not a human. LLMs are prediction engines. When you understand that an LLM is just super advanced autocomplete, that'll change your perspective. You're not asking a question. You're starting a pattern. If your pattern is vague, the AI guesses anything. But if it's more focused, you'll get way better results because you're hacking the probability.

## The Problem with Browser-Based AI

Tell me if this sounds like you because this is how I used to use AI. You're in the browser or app. You're asking questions. Research mode. You're diving deep into a project. Can't even see your scroll bar anymore. And this is your fifth chat because ChatGPT lost its context or its mind. You also created a few more chats with Claude and Gemini to make sure ChatGPT wasn't lying. And yeah, you tried to copy and paste some stuff into your notes app to keep track. That never works.

At this point, your project is a mess. Spread over 20 chats, two deep research sessions, and scattered notes. There's a better way to do this. Hear me out. It's in the terminal.

## Getting Started with Gemini CLI

We're going to play with Gemini CLI first. Why? Because it has a very generous free tier. That's right, you heard it, free. We can install it with one command. Go ahead and launch a terminal. It doesn't really matter where you launch it. Mac, Windows, Linux – all these terminal apps work everywhere.

For me, I'm going to use Windows with WSL or the Windows Subsystem for Linux. I'll launch my Ubuntu terminal and we'll copy and paste this command:

```bash
npm install -g @google/generative-ai-cli
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

First thing you'll do is get logged in with your Google account. Everyone has a Google account. And yes, this can be a free regular Gmail account. It's going to open your browser, sign in, and you're logged in.

Now, don't be scared. Go ahead, ask it a question like, "How do I make the best cup of coffee in the world?" That wasn't so bad, was it?

## The Terminal Advantage

But notice some superpowered things. First of all, we got Gemini 2.5 Pro, the latest and greatest model. Also, the browser doesn't show you this: 99% context left. Every chat you have with AI has a context window. The browser hides it from you. The terminal does not.

Also, your browser can't do this. Watch:

> I really want you to find the best way to make coffee. Research the top 10 sites, only reputable sources and then compile the results into a document named best-coffee-method.md and then create me a blog plan just an outline. I'll do the writing.

It's asking us a question. Do you want me to write a file for you? Yeah, dude. Go for it.

This thing can do everything a browser can do, but it has a superpower. It can access your computer. It can read and write files. Like, I'm not copying and pasting this. It's doing it for me. I mean, look, it actually made files on our computer. There they are.

Think about that for a second. It can access your Obsidian vault, all your notes, because those are just files sitting there on your hard drive. It can run bash and Python scripts. It can do mostly everything because we broke it out of the browser.

## The Game-Changer: Context Files

If we type in `/tools` and hit enter, you can see all that Gemini is allowed to do. You can even add more tools. But this feature right here is what made me switch from the browser to the terminal. Watch this. Type in `/init`. Just like that.

What it's doing right now is something powerful. It's creating a gemini.md file. And in the process, it analyzed our project, read our folder, read our files. What it just did there was create instructions for itself, context for what we're working on. Let's take a look at it:

```bash
cat gemini.md
```

And while we didn't do much in this project, it knows what's going on. And every time you launch Gemini, it's going to load that file as its context.

Let's test it. I'll open up another Gemini session in that same directory. This is a new conversation. Fresh context 100% left. Notice it's using our new gemini.md file. And I'll tell it this: "Write the intro for blog post one in the coffee series." No more context. Just that. It should know exactly what I'm talking about.

I didn't give it any context. It just knew. This is a new chat session. And as I work, I can just ask Gemini to update that file with my thoughts, research, decisions we made, the progress of our project.

I can close all this, start up a new session. It picks up where we left off. No reexplaining the context, no starting over, no more 20 scattered chats. We just had this one file that helps keep us organized. Everything you need. You're never paralyzed again.

## The Secret to Better Prompts: Context Engineering

Now, here's where most people fail with AI – they don't give it enough context. What Stanford calls "context engineering" is probably the most important technique I'm going to show you. It literally takes the guesswork out of prompting almost. And 2025 has kind of been the year of context. Like context is king.

Context engineering is just prompt engineering on steroids. It's basically asking: what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for?

This is the difference between writing, "give me some ideas for a birthday present under $30," and "give me five ideas for a birthday present. My budget is $30. The gift is for a 29-year-old who loves winter sports and has recently switched from snowboarding to skiing."

Here's a simple example from Jeremy Utley: "Write me a sales email" – that's a prompt. ChatGPT will say, "Absolutely. Here's a compelling email," and they'll write it immediately. But what a lot of people do is they say, "It sounds like AI. It doesn't really sound like me." And what I often say is, have you told it what you sound like?

If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer."

Whatever context or information you don't include, it's going to fill in those gaps itself. This is kind of the downside of LLMs. They're eager to please. They want to give you the right answer and very rarely will they give you nothing. So more context equals less hallucinations.

Here's a trick I learned from Anthropic: Give your AI permission to fail. Tell it it's okay if it doesn't have an answer. You will explicitly say, "If it's not in the context, you can't find the answer, say, 'I don't know.'" If you don't say that, it will lie to please you. And this is the number one fix for hallucinations.

The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

My advice: never assume it knows something. Never assume it has all the context. Always provide all the context every time. ABC. Always be contexting.

## Claude Code: The Daily Driver

I use Claude Code, which is Claude in the terminal, for pretty much everything. It's my default. And here's why. It has a feature that changes the game: Agents. Like, look at this. I have seven agents performing tasks right now in one terminal.

Now, Claude Code is not free, but I do have good news. If you already pay for Claude Pro, which starts at like 20 bucks a month, you can log into the terminal with this subscription and use it. So, yeah, you don't have to use API keys. And by the way, if you can only pay for one AI subscription, Claude Pro is the one I would choose.

Let's get it installed:

```bash
npm install -g @anthropic-ai/claude-cli
```

Then we'll launch Claude very similarly to Gemini. Just type in `claude` in your directory. It will prompt you to get logged in and then ask permission to access this folder. Yes, of course.

## The Power of Agents

Let's make a Claude agent right now. It's really simple. We'll do `/agents`. We'll get a terminal menu and let's create a home lab research expert. Create a new agent. We can tell it what we want it to be. Choose our model. Sonnet's great. There's our agent.

But what's the point of that? Because I kind of feel like we can just ask Claude to do research for us. You're right. But watch this. I'm going to give it this prompt and I'm calling the home lab agent:

> Create a comprehensive home lab setup guide. Make sure you reference the research we made.

It's going to use the home lab guru agent. There it is. There's our agent researching for us right now.

Here's why this is amazing. Actually kind of insane. So, Claude was like, "Cool. I've got a task, but it's not for me. I'm gonna delegate this task to one of my employees or one of my co-workers." And this is another Claude instance. He's giving him a fresh set of instructions and get this, a fresh context window.

You saw just now we have 200,000 tokens in our context window. We used 42% of it. This guy, he's got a fresh 200. That means the conversation we're having right now, me and the main Claude guy, it's protected. It doesn't get too bloated. I can give tasks to other sub agents and never have to leave this conversation.

## Advanced Prompting Techniques That Actually Work

Now that you've got the terminal setup, let's talk about advanced prompting techniques that will make your AI interactions exponentially better.

### Personas: Give Your AI Personality

Who is writing your content when you ask AI to write it? If you don't specify, it sounds like nobody. It's generic and soulless. That's where personas come in. We got to give this AI some personality.

Instead of just asking for an apology email, try: "You're a senior site reliability engineer for Cloudflare. You're writing to both customers and engineers. Write an apology letter or email."

When you think about it, it's not too strange. Let's say you're planning a trip to Japan. Who are you going to ask? Someone who has been to Japan, someone with experience planning trips, someone who loves Japan. That's the mindset we got to have when we're talking with AI. Who do we want crafting our response?

Assigning a role is one of the most foundational techniques because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

But better than just a generic role is being specific. Instead of "please review this correspondence," try: "I'd like you to be a professional communications expert. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this? How do the principles that Dale Carnegie taught affect and influence and impact this correspondence?"

### Chain of Thought: Show Your Work

Just like in math class, we're telling the LLM to take steps to think step by step before it answers. It looks like this: "Before writing this email, think through it step by step."

This does two things for us. First, accuracy goes way up because it's actually thinking before it writes. Also, trust goes up because we're seeing what it's doing, how it came to its conclusions.

Here's the science behind why this works: What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. It's thinking one word at a time. When you see the text scrolling in ChatGPT or Gemini, that's not some clever UX hack. That's literally how the model works.

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. So if you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

How do you do it? It doesn't require technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say: "Before you respond to my query, please walk me through your thought process step by step."

All the major AI providers now have this baked into their platforms. Look for buttons like "extended thinking" or "thinking mode." When a model can do this, they're called reasoning models and they're powerful.

### Few-Shot Prompting: Show, Don't Tell

Few-shot prompting is another foundational technique. The idea is that an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that.

The notion of few-shot prompting is effectively saying here's what a good output looks like to me. Think for a moment, what is a quintessential example of the kind of output I want to receive? For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email?

Giving real examples is a much better approach than using adjectives. And bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example.

If you struggle to think of bad examples, you can ask AI to help: "I'm trying to few-shot prompt a model. I've got a good example, but I struggle to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few-shot prompt?"

### Reverse Prompting: Let AI Ask the Questions

This is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating. You go, "Where did it get these sales numbers?" Well, here's my question: Did you give it your sales figures? How would it know?

But if you reverse prompt the model and say at the end of your prompt: "Help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

You basically give the model permission to ask you questions. This is part of the core of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

### Trees of Thought: Multiple Path Exploration

Where chain of thought explores one linear path, trees of thought explores multiple paths at once, like branches going on a tree. It enables the AI to do self-correction. It can go down one path and go, "Oh, dead end." Go down this path. "Oh, that's a good one."

Try this: "Brainstorm three distinct strategic approaches. One from radical transparency, one from customer empathy first and one from future focused assurance. Evaluate each branch. Synthesize them and then find the golden path."

### Battle of the Bots: Adversarial Validation

Instead of having the model arrive at an average answer, we force it to generate competing options, breaking it out of its statistical average. Generate a three round competition with three distinct personas. Have them write competing versions, critique each other, then collaborate on a final result.

The reason this works is because AI is normally better at critiquing or editing than original writing. So asking it to do this is actually tapping into its superpower.

## Getting Brutal Feedback (The Russian Judge Hack)

I don't really use these AI terminal tools to help me create. I use them to critique me and make me better. I got the brutal critic. I told him to be mean. So I had an issue where my AI was being way too agreeable. Like, I'd write something and be like, "Oh, Chuck, best thing you ever wrote." I'm like, "Ah, you're gaslighting me. Stop it."

I wanted something to be super mean. I wanted it to be hard to please. So that when it did tell me I did a good job, I knew it. Like, it was good. And that's what this thing does.

Here's Jeremy Utley's hack for this: "I always instruct the AI, I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

And then it's hilarious because it'll say "now channeling my inner Bulshvik," and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

The brutal critic has three personalities or three people that come in and roast it from different angles. Doing stuff like this saves me hours.

I want you to know this – it's not writing for me. I'm doing the writing because I like to keep that. I think that's important now with AI, but I do have AI roast me, help me stay on track because I get distracted. I might make some really bad creative decisions that aren't in line with what we're trying to do.

## Multiple AI Systems Working Together

Gemini, Claude Code, ChatGPT's Codex – I'm using all three right now to work on this video script. How? Two steps. First, as long as I open up Claude, Gemini, and Codex in the same directory, they're all using the same context. It's the same project.

The second thing I do is I make sure my context files are all synced up. They all say the same thing. So gemini.md, claude.md, and agents.md, which is what Codex uses – they're all the same.

I usually have a terminal open for each one while I'm working on a script or any kind of project. Watch this. I'll tell Claude to write a hook for this video. Authority angle. Write it to authority-hook.md. I'll have Gemini write a hook on a discovery angle, write it to discovery-hook.md, and then I'll have Codex review it.

I find ChatGPT is very good at analyzing things from a high view. Gemini and Claude are very good at the work, the deep work. They're all using the same context, different roles. I have three different AIs working on the same thing at the same time. No copying and pasting. They can see each other's work. They're working in the same directory.

## The Ultimate AI Training Ground: Difficult Conversations

One of the most powerful applications I've discovered is using AI as a flight simulator for difficult conversations. Jeremy Utley shared this incredible technique that uses three different AI windows to prepare for any challenging interaction.

Here's how it works: First, you use a personality profiler to analyze the person you need to speak with. Second, you have AI roleplay as that specific person. Third, you get objective feedback on your performance.

Let me show you exactly how this works. Say I need to have a difficult conversation with my sales leader Jim about commission attribution. I start with the personality profiler and give it context: "Hey, I'd love your help preparing for a conversation I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The profiler asks me questions: How would I describe Jim's communication style? He's quite direct and confrontational, typical East Coaster, sarcastic. What's my evidence? I know it came through our social team from a cold LinkedIn campaign. What's my best case outcome? I want Jim to back down and agree that the social team gets the commission.

Then the profiler generates instructions for me to paste into a new ChatGPT window to create the Jim character. I paste those instructions and suddenly I'm talking to AI-Jim. I can practice the conversation, see how he responds, adjust my approach.

But here's the genius part – after the conversation, I screenshot the entire interaction and paste it into a third AI window that's been trained to give me feedback. It grades my performance, tells me what I did well, what I could improve, and gives me specific talking points for the real conversation.

You can use this for any difficult conversation: performance reviews, salary negotiations, difficult feedback. It's like having a flight simulator for human interactions. And the beautiful thing is, historically the only time I get feedback is after I have the real conversation. This is the first time in history I can practice and get expert coaching before the stakes are real.

## Taking Control of Your Context

Are you seeing what's happening here? This is the craziest part about this. Everything I'm doing, talking with these three different AIs on a project – it's not tied in a browser. It's not tied in a GUI. It's just this folder right here on my hard drive. I can copy and paste that folder anywhere. All the work, all the decisions, all the context, it's mine.

And that's the difference. Nothing annoys me more than when ChatGPT tries to fence me in, give me that vendor lock-in so I can't leave. No, I reject that. I own my context. If a new, greater, better AI comes out, I'm ready for it because all my stuff is right here on my hard drive. I will use all AI. I will use the best AI. No one can stop me.

Leaving the browser, going to your terminal, puts you back in control, and it gives you better features.

## My Daily Workflow

This video was made with this process. First thing I want to show you is how things are synced up, specifically my Claude file, my Gemini file, and my agents file, which is Codex.

I rely on Claude to run my agent that will close out everything. When I'm done for the day, I'll go, "Hey, let's close this out." I'll mention my agent script session closer. This is one of those agents I keep as a personal agent. I use it for many projects.

It does a lot of stuff, but some of the key things it does: it'll gather everything we talked about, everything we did, and do a comprehensive summary. It will then update a session summary file. It will see if any core project files need to be updated. And if I'm talking with Claude, it will update every context file. Claude, Gemini, agents.

And then this is probably my favorite part. I commit my project to a GitHub repo. I treat my scripts and pretty much every project I work on in my life like code. We commit that change, give a reason for that change. So I can see a history of why what I did and why I did it. Maybe something breaks. I can go back to that change and reinstate it. That's the power of using GitHub with all your ideas.

## Open Source Alternative: OpenCode

There's a tool that's actually open source. You can use any model you want with this open-source alternative. And it might be the best tool of all of them. I'm still testing it. You also get Grok free, which is pretty sick. And a really powerful part of this is you can log in with your Claude Pro subscription and use it like Claude Code.

It's called OpenCode. We can install it with one command:

```bash
npm install -g opencode
```

You can use local models. This is the killer part. I don't think any other tool does this. We can edit a config file and use Llama 3.2 or any local model you have installed.

The fact that you can log in and use your Claude Pro subscription – that's next level because otherwise you're putting in an API key and you're paying per use. And that's a whole nightmare. I'd rather pay up front.

## The Meta Skill: Clarity of Thought

Here's the thing that all the experts told me, and it's the most important lesson in this entire article: All these foundational prompting techniques, learning how to talk to AI, all the tricks, they're all about clarity, about how to express yourself well.

The persona forces you to say, who is answering this? Where's the source of knowledge coming from? What's the perspective? Context forces us to say, "What are the facts? What does it need to know?" Chain of thought forces us to think about how the logic will flow. Few shot forces us to say, "This is what good looks like. Repeat that."

The techniques we're seeing here aren't magic tricks. You have to know how it's working, which boils down to how are you thinking? You have to get clear. Using all these techniques doesn't make the AI smarter. All that's happening here is you got clearer.

If the AI model's response is bad, treat everything as like a personal skill issue. The problem is me. When you're struggling with AI, it's not the AI's fault. It's not a prompting problem. It's that you don't really yet know how to think clearly. The AI can only be as clear as you are.

As Jeremy Utley puts it: "AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too."

So, the next time you're getting frustrated with AI and you're tempted to yell at ChatGPT, look in the mirror. It's you. It's a skill issue. You're not explaining yourself. So, stop. Get a notebook out. Get a pen or just open up a blank note and try to describe what you want to do, what you're wanting to accomplish. Think first, prompt second.

## The Future Is About Coaching, Not Coding

Here's what Jeremy Utley discovered that blew my mind: "The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences."

If you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

Where could AI go? Well, it's really a function of who can get unleashed. Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible are unthinkable, not because they're technologically impossible, but because they never occur to us personally.

As we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing what's possible. And it's really important that you exercise through implementing some of the things you've learned here.

## Why This Changes Everything

So how do you feel about your browser-based GUI AI now? Pretty bad, right? Kind of feels like hammer and chisel. Because now you can control your context. Break out of that browser, that chat window.

Don't let the terminal scare you. I mean, I know it's kind of intimidating if you're not used to working in the terminal. If you can get past that, this tool is for everyone. Everyone should be using this.

Nothing is stopping you from trying this right now. Gemini CLI, that's free. OpenCode, you can run local models if you're worried about that. And while Claude Code is paid, it's overpowered. You saw all those features. I use that every day.

Just you got to try it. Dip your toe in the water. It's fine. It's awesome. You will feel like you have a superpower and build whatever you want.

The point I want to hit home is that I made this for me. This is my own personal software, exactly my use case. What can you build for you that's just for you and your niche and whatever you're trying to make happen?

The tools I create are so powerful for me. I wake up every day feeling like I have superpowers. I want this for you.

And perhaps the most important thing you could do after reading this article is actually stop and do something that's already blown your mind. Don't just consume this information – implement it. Because that's how we expand what's possible, one person at a time.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2026-01-05 09:32:14

**Sources:**

1. [You've Been Using AI the Hard Way (Use This Instead)](https://www.youtube.com/watch?v=MsQACpcuTkU)
   - Channel: NetworkChuck
   - Views: 1,254,942
   - Comments: 4,222

2. [You SUCK at Prompting AI (Here's the secret)](https://www.youtube.com/watch?v=pwWBcsxEoLk)
   - Channel: NetworkChuck
   - Views: 429,923
   - Comments: 1,633

3. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 480,543
   - Comments: 476

**Cost Summary:**

- Total Input Tokens: 32,847
- Total Output Tokens: 15,980
- Total Tokens: 48,827
- **Total Cost: $0.3382**
- Model: Claude Sonnet 4


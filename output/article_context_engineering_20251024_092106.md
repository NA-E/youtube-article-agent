# Stanford's Practical Guide to 10x Your AI Productivity: Mastering Context Engineering

I joke: AI is bad software but it's good people. This simple observation has shaped my entire approach to artificial intelligence collaboration, and it's the key to unlocking productivity gains most people never achieve.

A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely, let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said "check back in a couple of days and I'll have it together." And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" I just started laughing because I hear this all the time from people.

If AI tells you "check back in 15 minutes," it means it doesn't want to say "I can't do it." You have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

## Understanding AI's Memory: The Context Window Challenge

Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or DeepSeek, they're kind of like us, you and me, in that they have memories. Short-term memory, which means they can remember things. But also, sometimes they can forget stuff.

Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said. But you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. Thankfully, you forgot that dumb thing I said. And sometimes we forget the entire point of the conversation.

ChatGPT does the same thing. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

Context windows are measured in tokens - how an AI counts the words you say to it. A sentence might be 133 characters or 26 words to us, but an LLM sees it as tokens. Different models calculate tokens differently, but the principle remains: when you hit that token limit, the AI starts forgetting things from earlier in your conversation.

When you say something to an LLM like, "Hey, I want coffee, but caffeine makes me jittery. What should I get?" it will do something eerily similar to how we process and think. It will use some fancy semantic math to decide which of these words is important, which is relevant both to the context of your entire conversation and to how the words relate to each other.

They essentially assign attention scores saying, "Hey, in this conversation, coffee is high, caffeine is high, jittery." But words like "I" or "me" kind of low relevance to the context. And we kind of do the same thing. We only remember the things that are relevant.

What's crazy is this process is pretty complex. All this math to assign attention scores. And it does this every time you send something to the LLM, every time you add to the conversation. Those larger contexts not only have insane memory requirements, they also have some pretty healthy computational requirements. Every time you add to that conversation, that math problem that has to run to figure out what's important gets bigger and it requires more processing power.

And that is why in those larger conversations, the LLM starts to hallucinate and it seems just a bit more slow. It's using a ton of memory and it's having to do some crazy math every time you talk to it.

There was a paper released called "Lost in the Middle" that showed us how LLMs are kind of like us with paying attention. Just like when you watch a long movie, you'll watch the first part then fall asleep and then wake up at the end - conversations with LLMs with large context showed the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. LLMs are falling asleep during a conversation, kind of.

Here's the crucial insight: when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat. The performance will be so much better. If you keep one conversation open with ChatGPT and just shoot the breeze - talking about coffee, the weather, asking it to explain quadratic equations - the AI is trying to weigh all of these different words and how relevant they are to the entire context of the conversation. No wonder it starts to hallucinate.

## The Foundation: Understanding Context Engineering

The first time I heard about context engineering was when Andre Karpathy tweeted about it. I think probably Toby Lutke, the CEO of Shopify, also referenced it as well. I started digging into it. It's just an evolution of prompt engineering. Really, context engineering is just prompt engineering on steroids.

It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example: "write me a sales email." That's a prompt. ChatGPT will say, "absolutely, here's a compelling email," and they'll write it immediately. Well, what a lot of people do is they say, "it sounds like AI. It doesn't really sound like me." And what I often say is, have you told it what you sound like? Most people go, "oh no, I haven't."

Context engineering, one way to think about it is it's telling AI what you sound like. If you say "Write me a sales email," it will. If you say "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email.

But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add "that also references our product specifications which were referenced in the call."

Your goal is to have an output that is as reliable per your specification as possible. But AI can't read your mind. And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind."

All of the stuff that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity: write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## The Revolution of Standardized AI Integration: MCP

While context engineering helps us communicate better with AI, there's been a fundamental challenge in how AI applications connect with the tools and data sources we use every day. That challenge has led to one of the most significant developments in AI workflow integration: the Model Context Protocol, or MCP.

The origin story is beautifully simple. As one of MCP's creators explains: "I worked on internal developer stuff and I got very quickly frustrated about having to copy things in and out of Claude Desktop and then copying things back and forth between my IDE and that's just really what I was thinking about like how can I solve copy and pasting the things I care about the most between these two applications."

MCP is just a way for putting your workflow into an AI application in a very simple way. It's a standardized protocol that defines how AI applications interact with tools, data sources, and context - essentially solving the "copy and paste" problem that has plagued AI workflows since the beginning.

The protocol standardizes three main components:
- **Tools**: Actions that the model can take in the world
- **Resources**: Raw data like files, text, or any context you want to give the model
- **Prompts**: Template prompts that users can trigger, often implemented as slash commands

What makes MCP special compared to just calling APIs directly? Models don't interact directly with APIs - they interact with prompts and tools and whatever you're giving the model to ingest. MCP standardizes how you take data from whether it's an API or some internal data source and actually give it to the model.

The breakthrough moment came during an internal hackathon at Anthropic. "Everyone was free to build basically whatever they wanted to build. But it turns out everyone just built an MCP and it was crazy. Like everyone's ideas were, oh, but what if we made this an MCP server?" Projects ranged from standard Slack integrations to someone who steered their 3D printer through MCP - bringing Claude into the real world in ways that seemed impossible before.

This organic adoption happened because of the standardization layer. The moment Claude integrated with MCP, server builders could create multiple servers knowing they would automatically work with the application. You only have to think about one side and not have to think about the other side.

There's a bit of magic when you teach Claude something new using an MCP server for the first time and you see it take action about something you care about. Within 5 minutes, you have something working. It almost feels like you take Claude out of the box, and instead of just outputting text, it's doing other things - calling applications, fetching data, or even operating physical devices.

The decision to make MCP open source was crucial. If you have a closed ecosystem for integrations, it isn't clear to server builders whether that AI application will be around forever or which ones they should invest in. By making it an open standard, you decrease the friction to building integrations. The value of building AI applications should focus on model intelligence and workflow, not on building integrations.

## The Coaching Mindset: Why the Best AI Users Aren't Coders

The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

When I realize that I'm dealing with a good person but bad software, then it changes how I approach it and I ask for volume and I iterate and I ask it to try again and I ask it to reconsider.

Some people are concerned about this concept of cognitive offloading - this observed phenomenon that humans actually kind of stop thinking or "fall asleep at the wheel" and people are concerned: is AI just making us dumber?

My feeling is AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

For example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

## Getting Honest Feedback: The Russian Judge Technique

AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

My kind of hack for this is I always instruct the AI: "I want you to do your best impression of a Cold War era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

And then it's of course hilarious because it'll say "now channeling my inner [Russian name]," and then it gives me like a 4.2. That is much better because now I have an insightful critical perspective.

## Five Essential Techniques for AI Mastery

### 1. Chain of Thought Reasoning: Making AI Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves.

The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning. And when you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model.

How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it: "Before you respond to my query, please walk me through your thought process step by step."

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you.

When you look at ChatGPT or Gemini and you see the text scrolling, that's not some clever UX hack. That's literally how the model works. It's thinking one word at a time. But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word.

By asking a model to think out loud or use chain of thought reasoning, you give the model the opportunity to bake all of its thought process about the task into its own answer. You know the answer to what are all of the assumptions that the model baked into its answer. And now you have the ability not only to evaluate the output, but also the thought process behind the output.

### 2. Few Shot Prompting: Teaching by Example

Few shot prompting is another very important technique. The idea with few shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that.

The notion of few shot prompting is effectively saying "here's what a good output looks like to me." Think for a moment: what is a quintessential example of the kind of output I want to receive?

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email?

If you don't give any guidance, it's going to sound like whatever it thinks the average response should sound like, and most of the time its intuition is wrong.

Bonus points if you actually give a bad example. If you say "please follow this good example and then steer clear of this bad example." Giving real examples is a much better approach than using adjectives.

### 3. Reverse Prompting: Let AI Ask the Questions

The other technique that I think is table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating. You go, "Where did it get these sales numbers?" Well, here's my question: Did you give it your sales figures? How would it know?

But if you reverse prompt the model and say at the end of your prompt: "help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

You basically give the model permission to ask you questions. This is part of the core of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me."

### 4. Role Assignment: Focusing AI's Knowledge

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus.

Very simply, if you say "you're a teacher," "you're a philosopher," "you're a reporter," "you're a theatrical performer," "molecular biologist" - each of those titles triggers all sorts of deep associations with knowledge on the internet.

You start to appreciate why simply giving a role helps because it starts to tell the AI: where in your vast knowledge bank do I want you to draw information and make connections?

Better than just "please review this correspondence" is saying "I'd like you to be a professional communications expert. And if you have a favorite professional communications expert, use them. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

### 5. Constraint Experimentation: Different Perspectives, Better Solutions

One of the simplest techniques that we teach is trying on different constraints. One of the best ways you can solve a problem as a human is by forcing yourself to try on a bunch of different constraints.

How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk?

Anytime you make an association, you're colliding different information sources. The same is true for an AI. An AI is basically making tons of connections through its own neural network. By giving it a role, you're telling it: where do you assume the best source of connection or collision is going to come from?

## The Flight Simulator: Preparing for Difficult Conversations

If I'm going to use AI to roleplay a difficult conversation, I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver to get objective feedback on the conversation.

This approach creates what I call a "flight simulator for difficult conversations." You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback.

Historically, the only time I get feedback is after I have the real conversation. This is the first time in history I can get comprehensive preparation for a specific situation and specific conversation I need to have in a way that AI is able to help me.

## Understanding AI's Cognitive Biases

I am obsessed with human cognitive bias. And the crazy thing that I've learned is AI demonstrates 100% of the predominant human biases.

The good news is if you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

## Practical Tips for Better AI Conversations

Here's a practical tip I've discovered: when you want to take content from a website and put it into an LLM to ask questions about it, don't just copy and paste the raw webpage. The format of all this information was not meant to be read by an LLM. It was meant to be read by humans.

There's a better way. Use tools that convert web pages into markdown that LLMs love - it's nice and clean. And as you're about to see, since LLMs do have a hard time paying attention, this definitely helps.

Remember: LLMs can be vulnerable to some creative prompting that can jailbreak out of their protection systems. The longer a conversation is, the more it can kind of forget what's in the middle, and the easier it will be for an attacker to hide some malicious stuff in there that could bypass its safety precautions.

## The Future of AI Integration: What's Next for MCP

Context windows are getting massive - GPT-4 has 128,000 tokens, Claude 3.5 has 200,000, and Gemini 2.5 from Google has 1 million tokens. Some models are even pushing toward 2 million tokens. But bigger isn't always better if the AI can't pay attention to all of it effectively.

The current state of MCP shows major players adopting it across their products, with an ecosystem of 10,000+ MCP server builders. We're at an interesting inflection point where initially MCP was mostly focused on developers and local experiences, but now we're seeing servers being hosted in the cloud through remote MCP and cloud AI integrations.

As models get more intelligent with releases like Claude 4 Opus and the new Sonnet, they can do longer running tasks. Some of the primitives built into MCP that haven't gotten much adoption yet - things related to statefulness and sampling - are going to become more useful. These are primitives that help in an agent's world but require models to have the intelligence for longer running tasks.

What's next for MCP includes better documentation and examples, key security primitives, and three major developments:

1. **Registry API**: This will allow models to search for additional servers that they can bring in on demand, enabling more agentic loops where the model isn't limited to predetermined tools.

2. **Long-running tasks**: Making it easy to do longer running things with MCP as models become more capable of extended operations.

3. **Elicitation**: How servers can go back and ask users for more information when needed, creating more interactive and dynamic workflows.

The hope is that we've hit on the right problem of providing context to LLMs and that the community can help guide the evolution. As one creator put it: "Just make something that people want to use and build this together with people who care about this."

## The Adjacent Possible: Where AI is Heading

One of my favorite quotes is from Nobel Prize-winning economist Thomas Schelling. He said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible are unthinkable - not because they're technologically impossible, but because they never occur to us personally.

As we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, we're increasing what innovation studies has called "the adjacent possible" for a long time. What is possible is just adjacent to what is.

We're witnessing something that feels like the birth of a new protocol. People are asking: is this what it was like to be around for HTTP? The hope is that we have hit on the right problem and thought far enough ahead that all the right building blocks are there for the community to guide us into the next steps.

## Taking Action: Your Next Steps

Perhaps the most important thing you could do with this information is actually hit stop and do something that's already blown your mind. The techniques I've shared - context engineering, chain of thought reasoning, few shot prompting, reverse prompting, role assignment, and constraint experimentation - are not theoretical concepts. They're practical tools that work immediately.

If you're a developer new to MCP, start by looking at an existing server that's online. Play around with it. See how it works with Claude AI or Claude Desktop. Get a feel for the interaction pattern first, then build your own. Start with the classic hello world - just do one tool that responds with hello world. Try the basic thing for prompts and resources before going into anything complex. Within 10 minutes, you can have something working.

The possibilities are endless. From MCP servers that bridge the gap to the real world - controlling synthesizers, 3D printers, or even doors with roleplay doormen - to creative applications like controlling Blender where Claude creates scenes by writing Blender scripts in real-time. Anything you could ping through an API can be wrapped in an MCP server and controlled with Claude or another LLM.

Start with one technique. Pick the conversation you need to have, the email you need to write, or the problem you need to solve. Apply these principles. Remember: AI is a mirror. If you approach it as a coach rather than expecting it to read your mind, if you give it context rather than hoping it will guess correctly, you'll unlock productivity gains that seemed impossible just a few years ago.

And remember the fundamental rule: when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat. The performance will be so much better.

The future belongs to those who can collaborate effectively with artificial intelligence. And that collaboration starts with understanding that we're not dealing with technology - we're dealing with a new kind of teammate that requires the same skills we use with human intelligence: clear communication, specific feedback, and the patience to iterate toward excellence. With protocols like MCP standardizing how these teammates connect to our tools and workflows, we're entering an era where the only limit is our imagination.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-24 09:21:06

**Sources:**

1. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 407,742
   - Comments: 433

2. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 153,233
   - Comments: 318

3. [The Model Context Protocol (MCP)](https://www.youtube.com/watch?v=CQywdSdi5iA)
   - Channel: Anthropic
   - Views: 209,448
   - Comments: 239

**Cost Summary:**

- Total Input Tokens: 24,304
- Total Output Tokens: 13,460
- Total Tokens: 37,764
- **Total Cost: $0.2748**
- Model: Claude Sonnet 4


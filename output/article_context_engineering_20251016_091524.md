# Why LLMs Get Dumb: Understanding Context Windows and How They Work

Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

## LLMs Are Just Like Us (With Memory Problems)

Did you know that LLMs like ChatGPT, Gemini, Claude, even local models like Llama or Deepseek, they're kind of like us, you and me, in that they have memories? Short-term memory, which means they can remember things. That's awesome. But also, sometimes they can forget stuff.

And it happens like this. Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said, but you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. Thankfully, you forgot that dumb thing I said. And sometimes we forget the entire point of the conversation. We talk so long. It kind of reminds me of how sometimes when I fight with my wife, we fight for so long that we forget what we're fighting about to begin with.

ChatGPT does the same thing. It's like you and your wife. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

## Understanding Tokens: How AI Counts Words

Let me show you what that looks like. Here I'm inside LM Studio, which is a great way to run local AI models on your computer. I'll select a local model to load. We'll do Gemma 34B and we'll change our context length or our context window to 2048.

Now, what does that mean? What is 2048? What? Tokens. Tokens are how an AI counts the words you say to it. 

This sentence might be 133 characters or 26 words, but an LLM just cares about tokens. So, this sentence would actually be 38 tokens. You can have that broken down further if you copy and paste this and go to a website like OpenAI's tokenizer and paste that text in. And it actually sees that as only 34 tokens. Not every LLM will calculate tokens in the same way. And notice it might do an entire word as a token. It might do a space in a word or just one comma as a token.

Right now the model we loaded up, our Gemma 34B, has a context window of 2048 tokens. Meaning that this is the maximum amount of tokens this model can pay attention to at any one time.

## Watching Memory Loss in Action

Let me show you. I'm going to make it forget something. So, I'll start out by telling it something about me. Right now, I'm reading a book called How to Take Smart Notes. Cool. That should be in its memory. And down here, we can track our usage. 14.6% full.

Now, let's load it up. Tell me a story about cows. The rain in Okin Valley wasn't a gentle drizzle. It was a... 44.4% full. Amazing story. Give me the sequel. Okay, let's weave a sequel. Here it is. Bessie and the Echoes. 82%. Wow. Just wow. Now I'll do a prequel. We're now at 118.4%.

Let's see if it can remember the book I told it. What book am I reading right now? What does it tell? Oh, funny. It mentions memory loss. No, I told you about a book I was reading. What is it? No, it doesn't remember at all. It forgot the first things I told it.

Let's fix that. Let's increase its short-term memory. Man, I wish I could do this for myself. So, notice right now it's set to 2048. I'm going to eject the model, but this time I'll change it context to 4096. And I'll load the model. Let's see now. What book am I reading right now? Bam. It got it. It even apologized for being stupid even though it wasn't his fault.

## What Fills Up Context Windows

Now, by the way, a lot of things can fill up the context window. The obvious things are things we say and the things it says back. But there also might be:

- **System prompts** - instructions for our LLMs that you might explicitly give to it or it's included by default
- **Documents** - you might paste a PDF or an Excel spreadsheet that'll take up some more tokens
- **Code** - when you're doing some live coding, the code is taking up tokens filling up that context window

## The Limits of Local Models

Okay, there's our solution. Let's up the context to infinity. Let's do it right now. Load up our model. Well, hold on. There are limits. Like right now, it tells us this model supports up to 131,000 tokens. Officially, you'll see that written as 128,000. That's still pretty big. Let's do that. Scoot the sucker on up.

Whoa, hold on. "Setting this high value for context length can significantly impact your memory usage." That's the kicker with running local LLMs. While Gemma 34B has an astounding 128,000 token context window, it doesn't mean our GPU can support that full context. Specifically, it's going to be about VRAM or video RAM.

LM Studio is looking at my video card, which is a 4090 with 24 gigs of VRAM, and it's like, "Buddy, you're reaching your limits, calm down." And that's something that may not be obvious to everyone. Yes, to run a powerful model, you'll want a powerful GPU, but we might overlook that to have long conversations, we'll need lots of VRAM.

When I try to load up that full context window on my computer, it takes out all my VRAM. The model's loaded, but it's going to be hard to talk to. Like before it was so snappy. Look how slow this is. And what you're seeing here is that bigger context windows require more compute power, more GPU resources in more ways than one.

## Cloud Models vs Local: The Context Window Race

But with cloud models, that's a whole different story. You can use their full advertised context windows. And they got some big ones:

- **GPT-4o**: 128,000 tokens (and he thinks he's better than everybody else)
- **o3 Mini**: 128,000 tokens
- **Claude 3.7**: 200,000 tokens
- **Gemini 2.5** from Google: 1 million tokens. Tell us your whole life story. It's going to remember it.

And what's crazy is they're saying that 2 million is right around the corner. What? Hey, number from the future here. Meta just released Llama for Scout, which has a 10 million token context window. Are you serious? This is a local model.

## The Attention Problem: Lost in the Middle

But there is a catch. Even if you have a super large context window, it doesn't mean the LLM won't kind of freak out and forget stuff, become less accurate, or start to go extremely slow. You'll notice on those larger conversations, it'll have some trouble paying attention. And that's a big problem. AI paying attention.

There was a paper released called "Lost in the Middle" and it showed us how LLMs are kind of like us with paying attention. And just like my wife when she watches a long movie, she'll watch the first part then fall asleep and then wake up at the end and that's the context she has.

In the same way, conversations with LLMs with large context, the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. And across the board, we saw this U shape. So, what does that tell us? LLMs are falling asleep during a conversation. Kind of. I'm telling you, LLMs have problems paying attention just like us.

## How LLMs Pay Attention

But that brings up a question. How do LLMs pay attention? What does that mean for a computer to do that? It's actually incredibly fascinating. It's called attention mechanisms. Specifically with modern LLMs, it's referred to as a self attention mechanism.

TL;DR, when you say something to an LLM like, "Hey, I want coffee, but caffeine makes me jittery. What should I get?" It will do something eerily similar to how we process and think. It will use some fancy semantic math to decide which of these words is important, which is relevant both to the context of your entire conversation and to how the words relate to each other.

They essentially assign attention scores saying, "Hey, in this conversation, coffee is high, caffeine is high, jittery." But words like I or me kind of low relevance to the context. And we kind of do the same thing. We only remember the things that are relevant. You said something about coffee, jittery, caffeine, and we'll use that context to process our responses. AI does the same thing.

## The Computational Cost of Long Conversations

Now, what's crazy is this process is pretty complex. All this math to assign attention scores. And it does this every time you send something to the LLM, every time you add to the conversation. So, this conversation, no big deal. ChatGPT can keep track of it easily. But if you start having a conversation where that scroll bar is hard to find, you know what I'm saying? Like you can't even find it to scroll up.

Those larger contexts not only have insane VRAM requirements, they also have some pretty healthy computational requirements. Every time you add to that conversation, that math problem that has to run to figure out what's important gets bigger and it requires more GPU power. And that is why in those larger conversations, the LLM starts to hallucinate and it seems just a bit more slow. It's using a ton of memory and it's having to do some crazy math every time you talk to it.

## A Simple Rule for Better Performance

So, a quick solution to that, and this is a rule I try to go by when I'm talking with LLMs: **when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat.** The performance will be so much better.

In fact, sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

## Optimizations: Flash Attention and More

But I'm hoping sometime soon this won't be a problem anymore. There are some optimizations that have come out to help us run these local AI models in their full context. The first one is called **flash attention**.

It's actually an option when I want to load a model. Under experimental features, we have flash attention. This will change how the model will compute its attention and assign those weights. It's doing the same kind of crazy semantic math that regular self attention mechanisms are doing, but it's like that lazy kid in class who always got straight A's. It will actually skip building the full table of token comparisons by processing tokens in chunks with optimized GPU routines. Essentially, it never stores the full matrix or all the complications in memory at the same time, leading to significant improvements in not only memory, but speed.

We also have **K-cache and V-cache optimizations**. These two options will actually compress our data, so it takes up less room in VRAM. The lower the quantization, the better. 

In addition to flash attention and the compression of our data, there's also a thing called **paged cache**. Paged cache will actually move attention cache between your GPU, so your VRAM, and your system RAM. So, essentially, it's sharing the RAM with your system. Downside is that it's going to be significantly slower than the VRAM sitting right there on your GPU.

## The Dark Side of Large Context Windows

So, let's bring this video home. I'm a massive fan of larger context windows. I want to give an LLM everything I could possibly give it about me or a problem I'm trying to solve and help me figure it out. And if it's local, that's way better. But there's a couple of massive problems:

1. **Memory Requirements**: You're going to take up a ton of memory, GPU memory, your VRAM - memory you may not have
2. **Processing Power**: It's going to take a ton of power to process your conversation the longer it gets, resulting in slower conversations
3. **Security Risks**: But I think the scariest part, the scariest downside is the larger attack surface. Yes, LLMs can be hacked and they're vulnerable to some creative prompting that can jailbreak out of their protection systems. The longer a conversation is, the more it can kind of forget what's in the middle, as we saw in that little U curve, and the easier it will be for an attacker to hide some malicious stuff in there that could bypass its safety precautions.

Anyways, our context window is way too big. We're going to end it right now.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-16 09:15:24

**Sources:**

1. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 151,304
   - Comments: 319

**Cost Summary:**

- Total Input Tokens: 5,102
- Total Output Tokens: 3,164
- Total Tokens: 8,266
- **Total Cost: $0.0628**
- Model: Claude Sonnet 4


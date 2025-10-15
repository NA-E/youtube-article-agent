"""
Transcript cleaning and punctuation logic.
Ported from TypeScript implementation in transcript-cleaner.ts
"""
import re
import html


def clean_transcript(raw_transcript: str) -> str:
    """
    Clean raw transcript by decoding HTML entities, normalizing whitespace and punctuation.

    Args:
        raw_transcript: Raw transcript text from RapidAPI

    Returns:
        Cleaned transcript text

    Raises:
        ValueError: If transcript is empty or None
    """
    print('\n========================================')
    print('[Transcript Cleaner] STARTING TRANSCRIPT CLEANING')
    print('========================================\n')

    # Type validation
    if not isinstance(raw_transcript, str):
        error_msg = f'Transcript must be a string, got {type(raw_transcript).__name__}'
        print(f'[Transcript Cleaner] ❌ ERROR: {error_msg}')
        raise TypeError(error_msg)

    # Empty string validation
    if not raw_transcript or raw_transcript.strip() == '':
        print('[Transcript Cleaner] ❌ ERROR: No transcript provided for cleaning')
        raise ValueError('No transcript available for cleaning')

    print(f'[Transcript Cleaner] Input length: {len(raw_transcript)} characters')

    print('[Transcript Cleaner] Step 1: Decoding HTML entities...')
    # Decode HTML entities using Python's html.unescape
    cleaned = html.unescape(raw_transcript)

    print('[Transcript Cleaner] Step 2: Normalizing whitespace...')
    # Replace multiple spaces with a single space
    cleaned = re.sub(r'\s+', ' ', cleaned)
    # Remove spaces before punctuation
    cleaned = re.sub(r'\s([.,!?;:])', r'\1', cleaned)

    print('[Transcript Cleaner] Step 3: Normalizing punctuation...')
    # Normalize repeated punctuation (e.g., "!!" -> "!")
    cleaned = re.sub(r'([.,!?;:])\1+', r'\1', cleaned)
    # Remove stray special characters at the start or end
    cleaned = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', cleaned)
    # Trim leading and trailing spaces
    cleaned = cleaned.strip()

    cleaned_length = len(cleaned)
    print('[Transcript Cleaner] ✓ Cleaning completed')
    print(f'[Transcript Cleaner] Output length: {cleaned_length} characters')
    print(f'[Transcript Cleaner] Reduction: {len(raw_transcript) - cleaned_length} characters')
    print(f'[Transcript Cleaner] Preview: {cleaned[:100]}...')
    print('\n========================================')
    print('[Transcript Cleaner] TRANSCRIPT CLEANING COMPLETED')
    print('========================================\n')

    return cleaned


def add_punctuation(cleaned_transcript: str) -> str:
    """
    Add missing punctuation to cleaned transcript.
    Splits into sentences and ensures each ends with proper punctuation.

    Args:
        cleaned_transcript: Cleaned transcript text

    Returns:
        Transcript with proper punctuation

    Raises:
        ValueError: If transcript is empty or None
    """
    print('\n========================================')
    print('[Punctuation Adder] STARTING PUNCTUATION ADDITION')
    print('========================================\n')

    # Type validation
    if not isinstance(cleaned_transcript, str):
        error_msg = f'Transcript must be a string, got {type(cleaned_transcript).__name__}'
        print(f'[Punctuation Adder] ❌ ERROR: {error_msg}')
        raise TypeError(error_msg)

    # Empty string validation
    if not cleaned_transcript or cleaned_transcript.strip() == '':
        print('[Punctuation Adder] ❌ ERROR: No transcript provided for punctuation')
        raise ValueError('No transcript available for punctuation processing')

    print(f'[Punctuation Adder] Input length: {len(cleaned_transcript)} characters')

    print('[Punctuation Adder] Step 1: Splitting into sentences...')
    # Split into potential sentences based on common sentence boundaries
    # Pattern: lowercase/number followed by space and uppercase letter
    sentences = re.split(r'(?<=[a-z0-9])\s+(?=[A-Z])', cleaned_transcript)

    print(f'[Punctuation Adder] Found {len(sentences)} potential sentences')

    print('[Punctuation Adder] Step 2: Adding missing punctuation...')
    processed_sentences = []
    for index, sentence in enumerate(sentences):
        sentence = sentence.strip()

        # Add a full stop if the sentence doesn't end with punctuation
        if not re.search(r'[.!?]$', sentence):
            sentence += '.'

        if index < 3:
            print(f'[Punctuation Adder] Sentence {index + 1}: {sentence[:50]}...')

        processed_sentences.append(sentence)

    print('[Punctuation Adder] Step 3: Joining sentences...')
    result = ' '.join(processed_sentences)

    result_length = len(result)
    print('[Punctuation Adder] ✓ Punctuation addition completed')
    print(f'[Punctuation Adder] Output length: {result_length} characters')
    print(f'[Punctuation Adder] Preview: {result[:150]}...')
    print('\n========================================')
    print('[Punctuation Adder] PUNCTUATION ADDITION COMPLETED')
    print('========================================\n')

    return result


def process_transcript(raw_transcript: str) -> str:
    """
    Full transcript processing pipeline: clean and add punctuation.

    Args:
        raw_transcript: Raw transcript text from RapidAPI

    Returns:
        Fully processed transcript

    Raises:
        ValueError: If transcript is empty or None
    """
    print('\n╔════════════════════════════════════════╗')
    print('║   TRANSCRIPT PROCESSING PIPELINE       ║')
    print('╚════════════════════════════════════════╝\n')

    cleaned = clean_transcript(raw_transcript)
    with_punctuation = add_punctuation(cleaned)

    print('╔════════════════════════════════════════╗')
    print('║   TRANSCRIPT PROCESSING COMPLETED      ║')
    print('╚════════════════════════════════════════╝\n')

    return with_punctuation

from pydub import AudioSegment


def split_audio(audio_path, split_length=60):
    audio = AudioSegment.from_wav(audio_path)

    length_audio = len(audio)
    start = 0
    # In Milliseconds, as pydub works in Milliseconds
    split_length = split_length * 1000

    end = 0
    counter = 0

    # End is greater than length then stop
    while start < length_audio:
        # Set end of the audio chunk
        end += split_length

        print(f"start: {start} end: {end}")

        chunk = audio[start:end]

        # Name of the chunk
        filename = f'chunk{counter}.wav'

        # Store chunk in destination directory
        chunk.export(filename, format="wav")

        # Print information
        print(f"Processing {filename}...")

        counter += 1
        start += split_length


# Replace with your .wav file
audio_file_path = "audio_file_path"
split_audio(audio_file_path)
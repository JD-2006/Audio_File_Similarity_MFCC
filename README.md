# Audio_File_Similarity_MFCC
Compare audio files with similarity plot

I use this script to compare my inferences from Retrieval-based-Voice-Conversion-WebUI

Here is a comparison of two files, with two lengths and different speakers. It has a score of 136.608.
![Figure_1-136 608](https://github.com/JD-2006/Audio_File_Similarity_MFCC/assets/85276310/71e80c18-c93b-4708-a094-79621d0db654)

These two are same length and same speaker. Lower score is better. So 75.759 is closer.
![Figure_2-75 759](https://github.com/JD-2006/Audio_File_Similarity_MFCC/assets/85276310/71af6c42-16e9-4a17-aedd-253387988e06)

And this one closer still with a score of 33.842.
![Figure_3-33 842](https://github.com/JD-2006/Audio_File_Similarity_MFCC/assets/85276310/72bafc1b-d212-4c9e-86a7-478369cd26be)

If you get "ModuleNotFoundError: No module named 'dtw'" error, pip install dtw-python.

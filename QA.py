
from Util import getNonMatching
from Util import makeBigramMap
from Util import getPercentage
from Util import allSentencesPerplexityUnderUnigram
from Util import allSentencesPerplexityUnderBigram
from Util import allSentencesPerplexityUnderBigramSmoothing
from Util import returnLogProbability


TAB = "\t\t"


def qa1(brownTraining):
    print("Ans #1: unique tokens in training file with <s>, </s> and <unk> :", brownTraining.replacedUniqueToken)


def qa2(brownTraining):
    print("Ans #2: total tokens in training file with :", brownTraining.actualTotalToken)


def qa3(brownTraining, brownTest, learnerTest):
    print("Ans #3: non matching percentage of types and tokens of tests with training before mapping <unk> :")

    t1 = getNonMatching(brownTraining.actualTokenMap.keys(), brownTest.actualTokenMap.keys(), brownTest.actualTokenMap)
    print(TAB, brownTraining.filename, "->", brownTest.filename, ":", t1, "types % ", getPercentage(t1[0], brownTest.actualUniqueToken),
          "-> tokens % ", getPercentage(t1[1], brownTest.actualTotalToken))

    t2 = getNonMatching(brownTraining.actualTokenMap.keys(), learnerTest.actualTokenMap.keys(), learnerTest.actualTokenMap)
    print(TAB, brownTraining.filename, "->", learnerTest.filename, ":", t2, "types % ", getPercentage(t2[0], learnerTest.actualUniqueToken),
          "-> tokens % ", getPercentage(t2[1], learnerTest.actualTotalToken))


def qa4(bigramBrownTraining, brownTraining, brownTest, learnerTest):
    print("Ans #4: non matching percentage Bigram of types and tokens of tests with training including <unk> :")

    bigramBrownTest = makeBigramMap(brownTest.replacedLines)
    bigramLearnerTest = makeBigramMap(learnerTest.replacedLines)

    t1 = getNonMatching(bigramBrownTraining.biTokenMap.keys(), bigramBrownTest.keys(), bigramBrownTest)
    print(TAB, brownTraining.modifiedFilename, "->",
          brownTest.modifiedFilename, ":", t1, "types % ", getPercentage(t1[0], len(bigramBrownTest)),
          "-> tokens % ", getPercentage(t1[1], sum(bigramBrownTest.values())))

    t2 = getNonMatching(bigramBrownTraining.biTokenMap.keys(), bigramLearnerTest.keys(), bigramLearnerTest)
    print(TAB, brownTraining.modifiedFilename, "->",
          learnerTest.modifiedFilename, ":", t2, "types % ", getPercentage(t2[0], len(bigramLearnerTest)),
          "-> tokens % ", getPercentage(t2[1], sum(bigramLearnerTest.values())))


def qa5(sentences, unigramBrownTraining, bigramBrownTraining, bigramSmoothingBrownTraining):
    print("Ans #5: Log probabilities of below sentences under 3 models.")

    print(TAB, sentences[0], "-> Under Unigram: ",
          returnLogProbability(unigramBrownTraining.calUnigramSentenceProbability(sentences[0])))
    print(TAB, sentences[0], "-> Under Bigram: ",
          returnLogProbability(bigramBrownTraining.calBigramSentenceProbability(sentences[0])))
    print(TAB, sentences[0], "-> Under Bigram Smoothing: ",
          returnLogProbability(bigramSmoothingBrownTraining.calBigramSmoothingSentenceProbability(sentences[0])))
    print()
    print(TAB, sentences[1], "-> Under Unigram: ",
          returnLogProbability(unigramBrownTraining.calUnigramSentenceProbability(sentences[1])))
    print(TAB, sentences[1], "-> Under Bigram: ",
          returnLogProbability(bigramBrownTraining.calBigramSentenceProbability(sentences[1])))
    print(TAB, sentences[1], "-> Under Bigram Smoothing: ",
          returnLogProbability(bigramSmoothingBrownTraining.calBigramSmoothingSentenceProbability(sentences[1])))
    print()
    print(TAB, sentences[2], "-> Under Unigram: ",
          returnLogProbability(unigramBrownTraining.calUnigramSentenceProbability(sentences[2])))
    print(TAB, sentences[2], "-> Under Bigram: ",
          returnLogProbability(bigramBrownTraining.calBigramSentenceProbability(sentences[2])))
    print(TAB, sentences[2], "-> Under Bigram Smoothing: ",
          returnLogProbability(bigramSmoothingBrownTraining.calBigramSmoothingSentenceProbability(sentences[2])))


def qa6(sentences, unigramBrownTraining, bigramBrownTraining, bigramSmoothingBrownTraining):
    print("Ans #6: Perplexity of below sentences under 3 models.")

    print(TAB, sentences[0], "-> Under Unigram: ", unigramBrownTraining.calUnigramSentencePerplexity(sentences[0]))
    print(TAB, sentences[0], "-> Under Bigram: ", bigramBrownTraining.calBigramSentencePerplexity(sentences[0]))
    print(TAB, sentences[0], "-> Under Bigram Smoothing: ",
          bigramSmoothingBrownTraining.calBigramSmoothingSentencePerplexity(sentences[0]))
    print()
    print(TAB, sentences[1], "-> Under Unigram: ", unigramBrownTraining.calUnigramSentencePerplexity(sentences[1]))
    print(TAB, sentences[1], "-> Under Bigram: ", bigramBrownTraining.calBigramSentencePerplexity(sentences[1]))
    print(TAB, sentences[1], "-> Under Bigram Smoothing: ",
          bigramSmoothingBrownTraining.calBigramSmoothingSentencePerplexity(sentences[1]))
    print()
    print(TAB, sentences[2], "-> Under Unigram: ", unigramBrownTraining.calUnigramSentencePerplexity(sentences[2]))
    print(TAB, sentences[2], "-> Under Bigram: ", bigramBrownTraining.calBigramSentencePerplexity(sentences[2]))
    print(TAB, sentences[2], "-> Under Bigram Smoothing: ",
          bigramSmoothingBrownTraining.calBigramSmoothingSentencePerplexity(sentences[2]))


def qa7(unigramBrownTraining, bigramBrownTraining, bigramSmoothingBrownTraining, brownTest, learnerTest):
    print("Ans #7: ")
    print(TAB, "Perplexity of all '" + str(brownTest.modifiedFilename) + "' sentences under 'Unigram' model ->",
          allSentencesPerplexityUnderUnigram
          (brownTest.replacedLines, unigramBrownTraining, brownTest.replacedTotalToken))
    print(TAB, "Perplexity of all '" + str(learnerTest.modifiedFilename) + "' sentences under 'Unigram' model ->",
          allSentencesPerplexityUnderUnigram
          (learnerTest.replacedLines, unigramBrownTraining, learnerTest.replacedTotalToken))
    print()

    print(TAB, "Perplexity of all '" + str(brownTest.modifiedFilename) + "' sentences under 'Bigram' model ->",
          allSentencesPerplexityUnderBigram
          (brownTest.replacedLines, bigramBrownTraining, brownTest.replacedTotalToken))
    print(TAB, "Perplexity of all '" + str(learnerTest.modifiedFilename) + "' sentences under 'Bigram' model ->",
          allSentencesPerplexityUnderBigram
          (learnerTest.replacedLines, bigramBrownTraining, learnerTest.replacedTotalToken))
    print()

    print(TAB, "Perplexity of all '" + str(brownTest.modifiedFilename) + "' sentences under 'BigramSmoothing' model ->",
          allSentencesPerplexityUnderBigramSmoothing
          (brownTest.replacedLines, bigramSmoothingBrownTraining, brownTest.replacedTotalToken))
    print(TAB, "Perplexity of all '" + str(learnerTest.modifiedFilename) + "' sentences under 'BigramSmoothing' model ->",
          allSentencesPerplexityUnderBigramSmoothing
          (learnerTest.replacedLines, bigramSmoothingBrownTraining, learnerTest.replacedTotalToken))
    print()






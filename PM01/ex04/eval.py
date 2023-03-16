class Evaluator:
    def zip_evaluate(coefs: list, words: list) -> float:
        if (len(coefs) != len(words)):
            return -1
        acum = 0.0
        for (coef, word) in zip(coefs, words):
            acum += coef * len(word)
        return acum

    def enumerate_evaluate(coefs: list, words: list) -> float:
        if (len(coefs) != len(words)):
            return -1
        acum = 0.0
        for (inx, word) in enumerate(words):
            acum += len(word) * coefs[inx]
        return acum


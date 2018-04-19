# Entry point for evaluating features.

from features.LIWC.liwc import liwc_score

if __name__ == "__main__":
    inp_data = "How much wood would a woodchuck chuck if they could throw it out of the park?"
    l = liwc_score()
    print(l.get_liwc_score(inp_data))
from scripts.preprocess import main as preprocess
from scripts.train import main as train
from scripts.optimize import main as optimize
from scripts.evaluate import main as evaluate
from scripts.build_database import main as build_database



def main():
    preprocess()
    train()
    optimize()
    evaluate()
    build_database()

if __name__ == "__main__":
    main()
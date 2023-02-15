from Map import Map
import argparse
from reinforcement_trainer import ReinforcementTrainer

from evolutionary_trainer import EvolutionaryTrainer


class Game:
    evo_auto_play = False

    def __init__(self):
        self.map = Map()
        self.colliders = self.map.collider_lines
        self.wall_rects = self.map.wall_rects
        self.result_file = '.gif'
        self.best = 0

    def run_reinfocement(self):
        trainer = ReinforcementTrainer(self.map)
        trainer.train()

    def run_evo(self, plotOrNot, evalOrNot, checkPoint):
        trainer = EvolutionaryTrainer(self.map)
        if evalOrNot:
            trainer.evaluation(checkPoint)
        else:
            trainer.train(plotOrNot)


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rl', type=str2bool, default=False, help='Will train the car with reinforcement learning, \
    otherwise will train the car with genetic algorithm')
    parser.add_argument('--auto_play', type=str2bool, default=False, help='Will play the gif after each generation automatically, \
    only applicable for evolutionary method')
    parser.add_argument('--save_gif', type=str2bool, default=False, help='Will save the plot.')
    parser.add_argument('--evaluate', type=str2bool, default=False, help='Evaluate or not.')
    parser.add_argument('--checkPoint', type=str, default=None, help='Evaluate with checkpoint.')

    opt = parser.parse_args()
    if opt.auto_play:
        Game.evo_auto_play = True

    if opt.rl:
        Game().run_reinfocement()
    else:
        Game().run_evo(opt.save_gif, opt.evaluate, opt.checkPoint)


if __name__ == "__main__":
    main()

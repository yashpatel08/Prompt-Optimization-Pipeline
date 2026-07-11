from app.models.experiment import Experiment


class ConsoleReporter:

    def display(self, experiments: list[Experiment], verbose: bool = False,):

        def format_latency(ms: float) -> str:
            if ms >= 1000:
                return f"{ms / 1000:.2f} s"
            return f"{ms:.1f} ms"

        for experiment in experiments:
            print("=" * 60)
            print(f"Model  : {experiment.model.name}")
            print(f"Prompt: {experiment.prompt.name} (v{experiment.prompt.version})")
            print("=" * 60)

            print(f"Accuracy : {experiment.accuracy:.2%}")
            print(f"Total        : {experiment.total}")
            print(f"Passed   : {experiment.passed}")
            print(f"Failed   : {experiment.failed}")
            print(f"Avg Latency : {format_latency(experiment.average_latency)}")
            print(f"Min Latency  : {format_latency(experiment.min_latency)}")
            print(f"Max Latency  : {format_latency(experiment.max_latency)}")
            print(f"Avg Tokens : {experiment.average_completion_tokens:.1f}")

            if not verbose:
                print()
                continue

            print("-" * 60)

            for result in experiment.results:
                status = "✓" if result.score == 1 else "✗"

                print(f"{status} {result.test_case.id}")
                print(f"Question : {result.test_case.input}")
                print(f"Expected : {result.test_case.reference}")
                print(f"Output   : {result.output}")
                print(f"Score    : {result.score}")
                print(f"Latency : {format_latency(result.latency_ms)}")
                print(f"Tokens   : {result.completion_tokens}")
                print()
            
        print("Run Summary")
        print("=" * 60)
        print(f"Models      : {len({e.model.id for e in experiments})}")
        print(f"Prompts     : {len({e.prompt.id for e in experiments})}")
        print(f"Experiments : {len(experiments)}")
        print(f"Test Cases  : {experiments[0].total}")
        print(f"Evaluations : {sum(e.total for e in experiments)}")
        print("=" * 60)

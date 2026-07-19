from app.models.trend import ExperimentTrend


class TrendReporter:

    def display(
        self,
        trends: list[ExperimentTrend],
    ):

        print()
        print("=" * 90)
        print("Historical Trends")
        print("=" * 90)

        for trend in trends:

            print()
            print(f"{trend.model} | {trend.prompt}")
            print("-" * 90)

            print(
                f"{'Run':<24}"
                f"{'Accuracy':>12}"
                f"{'Latency':>14}"
                f"{'Tokens':>12}"
            )

            print("-" * 90)

            for point in trend.history:

                print(
                    f"{point.run:<24}"
                    f"{point.accuracy:>11.2%}"
                    f"{point.latency/1000:>12.2f}s"
                    f"{point.tokens:>12.1f}"
                )

            print("-" * 90)

        print("=" * 90)
from app.models.regression_result import RegressionResult


class RegressionReporter:

    def display(
        self,
        reports: list[RegressionResult],
    ):

        print()
        print("=" * 100)
        print("Regression Detection")
        print("=" * 100)

        for report in reports:

            print()
            print(f"{report.model} | {report.prompt}")
            print("-" * 100)

            print(f"Regressions : {len(report.regressions)}")
            print(f"Improvements: {len(report.improvements)}")
            print(f"Unchanged   : {len(report.unchanged)}")

            if report.regressions:

                print()
                print("New Failures")
                print("-" * 100)

                for r in report.regressions:

                    print(f"❌ {r.test_case_id} ({r.task})")
                    print(f"   Score    : {r.previous_score:.1f} -> {r.latest_score:.1f}")
                    print(f"   Expected : {r.expected}")
                    print(f"   Previous : {r.previous_output}")
                    print(f"   Latest   : {r.latest_output}")
                    print()

            if report.improvements:

                print()
                print("Recovered")
                print("-" * 100)

                for r in report.improvements:

                    print(f"✅ {r.test_case_id} ({r.task})")
                    print(f"   Score    : {r.previous_score:.1f} -> {r.latest_score:.1f}")
                    print(f"   Expected : {r.expected}")
                    print(f"   Previous : {r.previous_output}")
                    print(f"   Latest   : {r.latest_output}")
                    print()

            print("-" * 100)

        print("=" * 100)
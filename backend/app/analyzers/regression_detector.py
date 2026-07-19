from app.models.run import Run
from app.models.regression import Regression
from app.models.regression_result import RegressionResult


class RegressionDetector:

    def detect(
        self,
        previous: Run,
        latest: Run,
    ) -> list[RegressionResult]:

        previous_map = {}

        for exp in previous.experiments:

            key = (exp.model.name, exp.prompt.name)

            previous_map[key] = exp

        reports = []

        for latest_exp in latest.experiments:

            key = (
                latest_exp.model.name,
                latest_exp.prompt.name,
            )

            if key not in previous_map:
                continue

            previous_exp = previous_map[key]

            previous_results = {r.test_case.id: r for r in previous_exp.results}

            regressions = []
            improvements = []
            unchanged = []

            for latest_result in latest_exp.results:

                if latest_result.test_case.id not in previous_results:
                    continue

                previous_result = previous_results[latest_result.test_case.id]

                regression = Regression(
                    test_case_id=latest_result.test_case.id,
                    task=latest_result.test_case.task,
                    previous_score=previous_result.score,
                    latest_score=latest_result.score,
                    expected=latest_result.test_case.reference,
                    previous_output=previous_result.output,
                    latest_output=latest_result.output,
                    status="",
                )

                if previous_result.score == 1 and latest_result.score == 0:

                    regression.status = "REGRESSION"
                    regressions.append(regression)

                elif previous_result.score == 0 and latest_result.score == 1:

                    regression.status = "IMPROVEMENT"
                    improvements.append(regression)

                else:

                    regression.status = "UNCHANGED"
                    unchanged.append(regression)

            reports.append(
                RegressionResult(
                    model=latest_exp.model.name,
                    prompt=latest_exp.prompt.name,
                    regressions=regressions,
                    improvements=improvements,
                    unchanged=unchanged,
                )
            )

        return reports

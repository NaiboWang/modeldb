import pytest

from verta import data_types


class TestConfusionMatrix:
    def test_confusion_matrix(self):
        attr = data_types.ConfusionMatrix(
            value=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            labels=["a", "b", "c"],
        )
        d = {
            "type": "verta.confusionMatrix.v1",
            "confusionMatrix": {
                "labels": ["a", "b", "c"],
                "value": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            },
        }
        assert attr._as_dict() == d
        assert attr == data_types.ConfusionMatrix._from_dict(d)

    def test_confusion_matrix_numpy(self):
        np = pytest.importorskip("numpy")
        attr = data_types.ConfusionMatrix(
            value=np.arange(1, 10).reshape((3, 3)),
            labels=np.array(["a", "b", "c"]),
        )
        assert attr._as_dict() == {
            "type": "verta.confusionMatrix.v1",
            "confusionMatrix": {
                "labels": ["a", "b", "c"],
                "value": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            },
        }


class TestDiscreteHistogram:
    def test_discrete_histogram(self):
        attr = data_types.DiscreteHistogram(
            buckets=["yes", "no"],
            data=[10, 20],
        )
        d = {
            "type": "verta.discreteHistogram.v1",
            "discreteHistogram": {
                "buckets": ["yes", "no"],
                "data": [10, 20],
            },
        }
        assert attr._as_dict() == d
        assert attr == data_types.DiscreteHistogram._from_dict(d)

    def test_discrete_histogram_numpy(self):
        np = pytest.importorskip("numpy")
        attr = data_types.DiscreteHistogram(
            buckets=np.array(["yes", "no"]),
            data=np.array([10, 20]),
        )
        assert attr._as_dict() == {
            "type": "verta.discreteHistogram.v1",
            "discreteHistogram": {
                "buckets": ["yes", "no"],
                "data": [10, 20],
            },
        }


class TestFloatHistogram:
    def test_float_histogram(self):
        attr = data_types.FloatHistogram(
            bucket_limits=[0, 3, 6],
            data=[10, 20],
        )
        d = {
            "type": "verta.floatHistogram.v1",
            "floatHistogram": {
                "bucketLimits": [0, 3, 6],
                "data": [10, 20],
            },
        }
        assert attr._as_dict() == d
        assert attr == data_types.FloatHistogram._from_dict(d)

    def test_float_histogram_numpy(self):
        np = pytest.importorskip("numpy")
        attr = data_types.FloatHistogram(
            bucket_limits=np.array([0, 3, 6]),
            data=np.array([10, 20]),
        )
        assert attr._as_dict() == {
            "type": "verta.floatHistogram.v1",
            "floatHistogram": {
                "bucketLimits": [0, 3, 6],
                "data": [10, 20],
            },
        }


class TestLine:
    def test_line(self):
        attr = data_types.Line(
            x=[1, 2, 3],
            y=[1, 4, 9],
        )
        d = {
            "type": "verta.line.v1",
            "line": {
                "x": [1, 2, 3],
                "y": [1, 4, 9],
            },
        }
        assert attr._as_dict() == d
        assert attr == data_types.Line._from_dict(d)

    def test_line_numpy(self):
        np = pytest.importorskip("numpy")
        attr = data_types.Line(
            x=np.array([1, 2, 3]),
            y=np.array([1, 4, 9]),
        )
        assert attr._as_dict() == {
            "type": "verta.line.v1",
            "line": {
                "x": [1, 2, 3],
                "y": [1, 4, 9],
            },
        }

    def test_line_from_tuples(self):
        attr = data_types.Line.from_tuples([(1, 1), (2, 4), (3, 9)])
        assert attr._as_dict() == {
            "type": "verta.line.v1",
            "line": {
                "x": [1, 2, 3],
                "y": [1, 4, 9],
            },
        }


class TestMatrix:
    def test_matrix(self):
        attr = data_types.Matrix([[1, 2, 3], [4, 5, 6]])
        d = {
            "type": "verta.matrix.v1",
            "matrix": {
                "value": [[1, 2, 3], [4, 5, 6]],
            },
        }
        assert attr._as_dict() == d
        assert attr == data_types.Matrix._from_dict(d)

    def test_matrix_numpy(self):
        np = pytest.importorskip("numpy")
        attr = data_types.Matrix(np.arange(1, 7).reshape((2, 3)))
        assert attr._as_dict() == {
            "type": "verta.matrix.v1",
            "matrix": {
                "value": [[1, 2, 3], [4, 5, 6]],
            },
        }


class TestTable:
    def test_table(self):
        attr = data_types.Table(
            data=[[1, "two", 3], [4, "five", 6]],
            columns=["header1", "header2", "header3"],
        )
        d = {
            "type": "verta.table.v1",
            "table": {
                "header": ["header1", "header2", "header3"],
                "rows": [[1, "two", 3], [4, "five", 6]],
            },
        }
        assert attr._as_dict() == d
        assert attr == data_types.Table._from_dict(d)

    def test_table_numpy(self):
        np = pytest.importorskip("numpy")
        attr = data_types.Table(
            data=np.arange(1, 7).reshape((2, 3)),
            columns=["header1", "header2", "header3"],
        )
        assert attr._as_dict() == {
            "type": "verta.table.v1",
            "table": {
                "header": ["header1", "header2", "header3"],
                "rows": [[1, 2, 3], [4, 5, 6]],
            },
        }

    def test_table_from_pandas(self):
        pd = pytest.importorskip("pandas")
        df = pd.DataFrame(
            [[1, "two", 3], [4, "five", 6]],
            columns=["header1", "header2", "header3"],
        )
        attr = data_types.Table.from_pandas(df)
        assert attr._as_dict() == {
            "type": "verta.table.v1",
            "table": {
                "header": ["header1", "header2", "header3"],
                "rows": [[1, "two", 3], [4, "five", 6]],
            },
        }

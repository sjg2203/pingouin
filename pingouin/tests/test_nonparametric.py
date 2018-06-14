import numpy as np
import pandas as pd
from pingouin.tests._tests_pingouin import _TestPingouin
from pingouin.nonparametric import (mwu, wilcoxon, kruskal, friedman)

np.random.seed(1234)
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)


class TestNonParametric(_TestPingouin):
    """Test nonparametric.py."""

    def test_mwu(self):
        """Test function mwu"""
        mwu(x, y, tail='one-sided')
        mwu(x, y, tail='two-sided')

    def test_wilcoxon(self):
        """Test function wilcoxon"""
        wilcoxon(x, y, tail='one-sided')
        wilcoxon(x, y, tail='two-sided')

    def test_friedman(self):
        """Test function friedman"""
        df = pd.DataFrame({'DV': np.r_[x, y, z],
                           'Time': np.repeat(['A', 'B', 'C'], 100)})
        friedman(data=df, dv='DV', within='Time')
        summary = friedman(data=df, dv='DV', within='Time',
                           export_filename='test_export.csv')
        # Compare with SciPy built-in function
        from scipy import stats
        Q, p = stats.friedmanchisquare(x, y, z)
        assert np.allclose(np.round(Q, 3), summary['Q']['Friedman'])
        assert np.allclose(p, summary['p-unc']['Friedman'])
        # Test with NaN
        df.loc[10, 'DV'] = np.nan
        friedman(data=df, dv='DV', within='Time')

    def test_kruskal(self):
        """Test function kruskal"""
        x[10] = np.nan
        df = pd.DataFrame({'DV': np.r_[x, y, z],
                           'Group': np.repeat(['A', 'B', 'C'], 100)})
        kruskal(data=df, dv='DV', between='Group')
        summary = kruskal(data=df, dv='DV', between='Group',
                          export_filename='test_export.csv')
        # Compare with SciPy built-in function
        from scipy import stats
        H, p = stats.kruskal(x, y, z, nan_policy='omit')
        assert np.allclose(np.round(H, 3), summary['H']['Kruskal'])
        assert np.allclose(p, summary['p-unc']['Kruskal'])
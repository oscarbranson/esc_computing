"""Check your answers to the 'Your turn' tasks in the exercise notebooks.

Load it at the top of a notebook with:

    from check import check, ___

Then fill in the ___ blanks in a 'Your turn' cell and run it. check() tells you whether your answer
is right, or gives you a hint, without telling you the answer. (This file needs to be in the same
folder as the notebooks.)
"""
import base64
import json

import numpy as np

___ = ...   # the blank in 'Your turn' cells: replace it with your answer

# the expected answers, encoded so that they aren't visible at a glance
_ANSWERS = json.loads(base64.b64decode(
    'eyJzZWNvbmRzIHBlciBkYXkiOiB7ImV4cGVjdGVkIjogODY0MDAsICJoaW50IjogIkEgZGF5IGhhcyAyNCBob3VycywgZWFj'
    'aCBvZiA2MCBtaW51dGVzLCBlYWNoIG9mIDYwIHNlY29uZHMuIn0sICJlYXJ0aCBtYXNzIjogeyJleHBlY3RlZCI6IDUuOTdl'
    'KzI0LCAiaGludCI6ICJJbiBlIG5vdGF0aW9uLCAnZTI0JyBtZWFucyAndGltZXMgMTAgdG8gdGhlIHBvd2VyIG9mIDI0Jywg'
    'd2l0aCBub3RoaW5nIGluIGJldHdlZW4uIn0sICJlYXJ0aCBkZW5zaXR5IjogeyJleHBlY3RlZCI6IDU1MTEsICJoaW50Ijog'
    'IkRpZCB5b3UgY29udmVydCB0aGUgcmFkaXVzIGZyb20ga20gdG8gbT8ifSwgImNvb2xpbmcgdGltZSI6IHsiZXhwZWN0ZWQi'
    'OiAzMi4zLCAiaGludCI6ICJEaWQgeW91IGRpdmlkZSBieSBwaSBzcXVhcmVkLCBhbmQgY29udmVydCBmcm9tIHNlY29uZHMg'
    'dG8gTXlyPyJ9LCAibWlkZGxlIHJvY2tzIjogeyJleHBlY3RlZCI6IFsiZ3Jhbml0ZSIsICJnbmVpc3MiLCAic2NoaXN0Il0s'
    'ICJoaW50IjogIlJlbWVtYmVyIHRoYXQgYSBzbGljZSBhOmIgc3RvcHMgYmVmb3JlIGIuIn0sICJ2ZW51cyI6IHsiZXhwZWN0'
    'ZWQiOiAidG9vIGhvdCIsICJoaW50IjogIllvdXIgaWYgc3RhdGVtZW50IHNob3VsZCBjb21wYXJlIFRfdmVudXMgd2l0aCAz'
    'NzMsIGFuZCBzZXQgdmVyZGljdCB0byBleGFjdGx5ICd0b28gaG90JyBvciAnZmluZScuIn0sICJwcmVzc3VyZXMiOiB7ImV4'
    'cGVjdGVkIjogWzAsIDI2NDg3MDAwLCAxMzI0MzUwMDAsIDI2NDg3MDAwMF0sICJoaW50IjogIkFyZSB5b3UgYXBwZW5kaW5n'
    'IHJobyAqIGcgKiBoIGZvciBlYWNoIGRlcHRoIGgsIHdpdGggcmhvID0gMjcwMCBhbmQgZyA9IDkuODE/IFRoZSBkZXB0aHMg'
    'YXJlIGFscmVhZHkgaW4gbWV0cmVzLiJ9LCAidG90YWwiOiB7ImV4cGVjdGVkIjogMTAsICJoaW50IjogIkxvb2sgYXQgd2hl'
    'cmUgdG90YWwgaXMgc2V0IHRvIDA6IGhvdyBtYW55IHRpbWVzIGRvZXMgdGhhdCBsaW5lIHJ1bj8ifSwgInNpbiAzMCI6IHsi'
    'ZXhwZWN0ZWQiOiAwLjUsICJoaW50IjogIkRpZCB5b3UgY29udmVydCAzMCBkZWdyZWVzIHRvIHJhZGlhbnMgZmlyc3Q/In0s'
    'ICJkYXRhIG1lYW4iOiB7ImV4cGVjdGVkIjogODIzLjQ1LCAiaGludCI6ICJVc2UgbnAubWVhbigpIG9uIHRoZSB3aG9sZSBv'
    'ZiBmYWtlX2RhdGEuIn0sICJ0ZW1wcyBpbiBLIjogeyJleHBlY3RlZCI6IFsyNzMuMTUsIDI5OC4xNSwgMzczLjE1LCAyMzMu'
    'MTVdLCAiaGludCI6ICJBZGQgMjczLjE1IHRvIHRoZSB3aG9sZSBhcnJheSBhdCBvbmNlOiBubyBsb29wIG5lZWRlZC4ifSwg'
    'ImJvaWxpbmciOiB7ImV4cGVjdGVkIjogMzczLjE1LCAiaGludCI6ICJXaGF0IGRvZXMgdGhlIGZ1bmN0aW9uIGdpdmUgYmFj'
    'az8gTG9vayBmb3IgYSByZXR1cm4gc3RhdGVtZW50LiJ9LCAia20gdG8gbWlsZXMgM2RwIjogeyJleHBlY3RlZCI6IDIuOTgz'
    'LCAiaGludCI6ICJEb2VzIHlvdXIgZnVuY3Rpb24gdXNlIGl0cyBuZHAgYXJndW1lbnQgd2hlbiBpdCByb3VuZHMsIHJhdGhl'
    'ciB0aGFuIGEgZml4ZWQgbnVtYmVyPyIsICJ0b2wiOiAxZS0wOX0sICJrbSB0byBtaWxlcyI6IHsiZXhwZWN0ZWQiOiAzLjAs'
    'ICJoaW50IjogIkRpdmlkZSB0aGUgZGlzdGFuY2UgYnkgMS42MDksIHRoZW4gcm91bmQgdGhlIHJlc3VsdCB0byBuZHAgZGVj'
    'aW1hbCBwbGFjZXMgd2l0aCByb3VuZCgpLiIsICJ0b2wiOiAxZS0wOX0sICJoYXJkbmVzcyI6IHsiZXhwZWN0ZWQiOiBbNi41'
    'LCA2LjAsIDUuNSwgNy4wXSwgImhpbnQiOiAiU2VsZWN0IHRoZSAnaGFyZG5lc3MnIGNvbHVtbiwgcmF0aGVyIHRoYW4gYSBy'
    'b3cuIn0sICJudW1iZXIgb2YgbWluZXJhbHMiOiB7ImV4cGVjdGVkIjogNCwgImhpbnQiOiAiRWFjaCBtaW5lcmFsIGlzIG9u'
    'ZSByb3c6IGhvdyBtYW55IHJvd3MgZG9lcyBkZm0gaGF2ZT8ifSwgInBpY2tlZCI6IHsiZXhwZWN0ZWQiOiAxOTE3LCAiaGlu'
    'dCI6ICJFYWNoIGNvbmRpdGlvbiBuZWVkcyBpdHMgb3duIGJyYWNrZXRzIGFyb3VuZCBpdCwgYXMgaW4gdGhlIGNlbGwgYWJv'
    'dmUuIn0sICJiYXNhbHRzIjogeyJleHBlY3RlZCI6IDI3MjIsICJoaW50IjogIkNvdW50IHRoZSByb3dzIG9mIGRmIChub3Qg'
    'ZGZfYmVzdCkgd2hlcmUgU2lPMiBpcyBiZWxvdyA1Mi4ifSwgInlvdW5nIGVydXB0aW9ucyI6IHsiZXhwZWN0ZWQiOiAxLjU1'
    'OTc4NTcxNDI4NTcxNDMsICJoaW50IjogIlNlbGVjdCB0aGUgcm93cyBvZiBkZl9lcnVwdCAob25lIHJvdyBwZXIgZXJ1cHRp'
    'b24pIHdpdGggYW4gYWdlIGJlbG93IDEwMDAsIHRoZW4gdGFrZSB0aGUgbWVhbiBvZiB0aGVpciB2b2x1bWUgY29sdW1uLiJ9'
    'LCAiY2FtYnJpZGdlIjogeyJleHBlY3RlZCI6IFswLjEyLCA1Mi4yXSwgImhpbnQiOiAiYXgucGxvdCgpIHRha2VzIHggKGxv'
    'bmdpdHVkZSkgZmlyc3QsIHRoZW4geSAobGF0aXR1ZGUpLiJ9LCAiaWNlIGNhcHMiOiB7ImV4cGVjdGVkIjogMTUsICJoaW50'
    'IjogInBvbHlfam9rdWxsKCkgZ2l2ZXMgYmFjayBhIGxpc3Qgb2YgcG9seWdvbnM6IGhvdyBsb25nIGlzIHRoYXQgbGlzdD8i'
    'fSwgImJpZyBlcnVwdGlvbnMiOiB7ImV4cGVjdGVkIjogMjcsICJoaW50IjogIlNlbGVjdCB0aGUgcm93cyBvZiBkZnZzIHdo'
    'ZXJlICdWb2x1bWUoa20zKScgaXMgZ3JlYXRlciB0aGFuIDEwLCB0aGVuIGNvdW50IHRoZW0uIn0sICJpbnRlcmNlcHQiOiB7'
    'ImV4cGVjdGVkIjogMC43MDYxODUyNDQ1Mzc5NTk0LCAidG9sIjogMWUtMDYsICJoaW50IjogIlRyeSBwcmludGluZyByZXMg'
    'dG8gc2VlIGFsbCB0aGUgcmVzdWx0cyBpdCBob2xkcy4ifSwgInNsb3BlIjogeyJleHBlY3RlZCI6IDAuMDAxMjQ2LCAiaGlu'
    'dCI6ICJUcnkgcHJpbnRpbmcgcmVzIHRvIHNlZSBhbGwgdGhlIHJlc3VsdHMgaXQgaG9sZHMuIn0sICJvbGQgbGFtYmRhIGFn'
    'ZSI6IHsiZXhwZWN0ZWQiOiA4Ny43LCAiaGludCI6ICJVc2UgbG1iZF9vbGQgaW4gdGhlIGFnZSBlcXVhdGlvbiwgYW5kIGRp'
    'dmlkZSBieSAxZTYgdG8gY29udmVydCB5ZWFycyB0byBNeXIuIn0sICJhZ2UiOiB7ImV4cGVjdGVkIjogODkuNCwgImhpbnQi'
    'OiAiTG9vayBhZ2FpbiBhdCB3aGF0IGdvZXMgaW5zaWRlIHRoZSBsb2cgaW4gdGhlIGlzb2Nocm9uIGVxdWF0aW9uLiJ9LCAi'
    'c2NhbGVkIGVycm9yIjogeyJleHBlY3RlZCI6IDEyLjksICJoaW50IjogIk11bHRpcGx5IGFnZV9lcnIgYnkgdGhlIHNxdWFy'
    'ZSByb290IG9mIG1zd2QsIHRoZW4gY29udmVydCBmcm9tIHllYXJzIHRvIE15ci4ifSwgInNlZWQgcm9sbHMiOiB7ImV4cGVj'
    'dGVkIjogWzYsIDEsIDEsIDYsIDNdLCAiaGludCI6ICJEaWQgeW91IHNldCB0aGUgc2VlZCB0byA0MiBmaXJzdCwgYW5kIHVz'
    'ZSByYW5kLnJhbmRpbnQoMSwgNik/In0sICJub3JtYWwgc3RkIjogeyJleHBlY3RlZCI6IDIsICJ0b2wiOiAwLjAzLCAiaGlu'
    'dCI6ICJVc2UgbnAuc3RkKCkgb24gdGhlIHNhbWUgZHJhd3MuIn0sICJub3JtYWwgbWVhbiI6IHsiZXhwZWN0ZWQiOiA1LCAi'
    'dG9sIjogMC4wMiwgImhpbnQiOiAibnAucmFuZG9tLm5vcm1hbCgpIHRha2VzIHRoZSBtZWFuLCB0aGUgc3RhbmRhcmQgZGV2'
    'aWF0aW9uIGFuZCB0aGUgbnVtYmVyIG9mIGRyYXdzLiBUaGVuIHVzZSBucC5tZWFuKCkgb24gdGhlIGRyYXdzLiJ9LCAiZGll'
    'IjogeyJleHBlY3RlZCI6IDMuNSwgImhpbnQiOiAiV2hpY2ggbnVtYmVycyBjYW4gbnAucmFuZG9tLnJhbmRpbnQoMCwgNikg'
    'Z2l2ZT8gTG9vayBiYWNrIGF0IHRoZSBib3ggYWJvdXQgdXBwZXIgbGltaXRzLiJ9LCAic2V2ZW4iOiB7ImV4cGVjdGVkIjog'
    'MC4xNjY2NjY2NjY2NjY2NjY2NiwgInRvbCI6IDAuMDUsICJoaW50IjogIk1ha2UgZGllMiB0aGUgc2FtZSB3YXkgYXMgZGll'
    'MSwgdGhlbiB0YWtlIHRoZSBtZWFuIG9mIChkaWUxICsgZGllMiA9PSA3KS4ifSwgInN3aXRjaCI6IHsiZXhwZWN0ZWQiOiAw'
    'LjY2NjY2NjY2NjY2NjY2NjYsICJ0b2wiOiAwLjEsICJoaW50IjogIlRoZSB0aHJlZSBib3ggaW5kaWNlcyBhZGQgdXAgdG8g'
    'MCArIDEgKyAyID0gMy4gV2hpY2ggaW5kZXggaXMgbmVpdGhlciBwaWNrIG5vciBzaG93PyJ9fQ=='
).decode())


def _is_blank(answer):
    return answer is ___ or (isinstance(answer, (list, tuple)) and any(a is ___ for a in answer))


def check(task, answer):
    """Print ✓ if your answer to the named task is right, or a hint if it isn't."""
    if task not in _ANSWERS:
        print(f"✗ There's no task called {task!r}. Check the spelling of the task name.")
        return
    if _is_blank(answer):
        print('✗ Replace the ___ with your answer first.')
        return
    entry = _ANSWERS[task]
    expected, tol = entry['expected'], entry.get('tol', 0.01)
    try:
        ok = bool(np.allclose(answer, expected, rtol=tol, atol=0))
    except (TypeError, ValueError):
        try:
            ok = bool(answer == expected)
        except ValueError:
            ok = False
    if ok:
        print('✓ Correct!')
    else:
        print(f"✗ Not quite: you got {answer!r}. {entry.get('hint', 'Have another look.')}")

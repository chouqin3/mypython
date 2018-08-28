import sys, time
tic_start_g = []
def tic(msg = None, show = True):
    global tic_start_g
    if (msg is not None) and show:
        print >>sys.stderr, msg
    tic_start_g.append((msg, time.time()))
    print(tic_start_g)
d= {"one": 10, "two": 20, "three": 30}
total = float(sum(d.values()))
normd = dict((k, d[k]/total) for k in d)
for k,v in normd.items():
    # print(k)
    print(normd.get(k))
    print(normd.values())
def toc(s = None, show = True):
  """ end a timer and print (the elapsed time """
  global tic_start_g
  if len(tic_start_g) == 0:
    if show:
      print  ( 'toc() called without tic!')
    return
  msg, t = tic_start_g.pop()
  time.sleep(5.0)
  elapsed = time.time() - t
  if s is not None:
    msg = s
  if show:
    if msg is not None:
      print ('%.3f seconds' % elapsed)
    else:
      print  ('%.3f seconds123132' % elapsed)
  return elapsed

tic()
toc()



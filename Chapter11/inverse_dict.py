def inverse_dict(d):

	inverse=dict()

	for key in d:
		value=d[key]
		inverse.setdefault(value,[]).append(key)
	return inverse

print(inverse_dict({'a':1,'b':1,'c':2}))

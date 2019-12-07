from seisnn.pick import search_pick, get_pdf


def stream_preprocessing(stream, pick_list, geom):
    stream = signal_preprocessing(stream)
    stream = get_exist_picks(stream, pick_list)
    stream = get_pdf(stream)
    stream = get_stream_geom(stream, geom)
    return stream


def signal_preprocessing(stream):
    stream.detrend('demean')
    stream.detrend('linear')
    stream.normalize()
    stream.resample(100)
    return stream


def get_exist_picks(stream, pick_list):
    picks = search_pick(pick_list, stream)
    stream.picks = picks
    return stream


def get_stream_geom(stream, geom):
    station = stream.traces[0].stats.station
    stream.location = geom[station]
    return stream

import singer
from singer import Transformer, metadata

from tap_amazon_sp.streams import StreamClassSelector

LOGGER = singer.get_logger()


def sync(config, state, catalog):
    """ Sync data from tap source """

    with Transformer() as transformer:
        for stream in catalog.get_selected_streams(state):
            tap_stream_id = stream.tap_stream_id
            stream_obj = StreamClassSelector(config, stream)
            stream_schema = stream.schema.to_dict()
            stream_metadata = metadata.to_map(stream.metadata)

            LOGGER.info('Starting sync for stream: %s', tap_stream_id)

            state = singer.set_currently_syncing(state, tap_stream_id)
            singer.write_state(state)

            singer.write_schema(
                tap_stream_id,
                stream_schema,
                stream_obj.key_properties,
                stream.replication_key
            )

            state = stream_obj.sync(state, stream_schema, stream_metadata, transformer)
            singer.write_state(state)

    state = singer.set_currently_syncing(state, None)
    singer.write_state(state)

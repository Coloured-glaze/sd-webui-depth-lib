def preload(parser):
    parser.add_argument(
        "--depth-maps-dir",
        type=str,
        help="Path to directory with depth maps",
        default=None,
    )

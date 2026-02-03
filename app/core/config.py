from dataclasses import dataclass, field


@dataclass(frozen=True)
class _FGISArshinConfig:
    host: str = "fgis.gost.ru"
    request_retries: int = 3


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
@dataclass(frozen=True)
class _AppConfig:
    api: _FGISArshinConfig = field(default_factory=_FGISArshinConfig)


def get_config() -> _AppConfig:
    return _AppConfig()

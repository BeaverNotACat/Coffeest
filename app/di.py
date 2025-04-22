from dishka import Provider, Scope, make_container

singleton_provider = Provider(scope=Scope.APP)

container = make_container

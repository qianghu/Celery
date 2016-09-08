# Celery 3.1 文档
    English: http://docs.celeryproject.org/en/master/index.html
    中文: http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html

    # 选择中间人
    Celery 需要一个发送和接收消息的解决方案，其通常以独立服务形式出现， 称为 消息中间人。
    # RabbitMQ 功能完备、稳定、耐用，并且安装简便，是生产环境的绝佳选择。
        # RabbitMQ 是默认的中间人，所以除了需要你要使用的中间人实例的 URL 位置， 它并不需要任何额外的依赖或起始配置:
            >>> BROKER_URL = 'amqp://guest:guest@localhost:5672//'

        # 安装 RabbitMQ
            # Ubuntu
                $ sudo apt-get install rabbitmq-server

            # Mac OS X
                # 在安装之前确保你有最新的brew:
                $ brew update
                # 然后,安装RabbitMQ服务器:
                $ brew install rabbitmq
        # 设置 RabbitMQ
            # 要使用 Celery，我们需要创建一个 RabbitMQ 用户、一个虚拟主机，并且允许这个用户访问这个虚拟主机：
                $ sudo rabbitmqctl add_user myuser mypassword
                $ sudo rabbitmqctl add_vhost myvhost
                $ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"sudo rabbitmqctl status

    # 安装 Celery
    Celery 提交到了 Python Package Index（PyPI）上，所以可以用标准的 Python 工具，诸如 pip 或 easy_install 来安装：
        $ pip install celery



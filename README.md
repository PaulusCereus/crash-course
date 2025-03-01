# Мое первое знакомство с `git`, `github`, `markdown`

# Что успели изучить

## Проверка работоспособности и версии git

```bash
git --version
```

## Настройка git с помощью конфигурации имени и почты

```bash
git config --global user.name "My Name"
git config --global user.email "myemail@example.com"
```

## Проверка настроек 

```bash
git config --list
```

## Проверка текущего статуса репозитория

```bash
git status
```

## Проверка всех логов (история коммитов)

```bash
git log
```


## Добавление файлов в отслеживаемое состояние

```bash
git add filename1 filename2 filename3
```

## Подтверждение изменений всех файлов в отслеживаемом состоянии

```bash
git commit -m "My message of this commit"
```
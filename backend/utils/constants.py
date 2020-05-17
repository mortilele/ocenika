NO_IMAGE = 'nologo.png'
NO_AVATAR = 'noavatar.png'
REVIEW_ALREADY_SUBMITTED = 'Вы уже оставляли отзыв данному преподавателю'


ON_MODERATION = 'На модерации'
DECLINED = 'Отказан'
ACCEPTED = 'Принят'

REVIEW_STATUSES = (
    (ON_MODERATION, ON_MODERATION),
    (ACCEPTED, ACCEPTED),
    (DECLINED, DECLINED)
)


ACTIVE = 'Активный'

CONFIRM_USER = 'Пожалуйста подтвердите вашу Email почту!'
CONFIRMATION_SEND = 'Видимо, Вы ранее не регистрировались, ничего страшного мы сделали это за вас, вам остается ' \
                    'подтвердить вашу почту, и прикрепить транскрипт '
REVIEW_ON_MODERATION = 'Ваш отзыв успешно отправлен'
ASSIGN_TRANSCRIPT = 'Пожалуйста прикрепите транскрипт'

UPDATE_TRANSCRIPT = 'Пожалуйста, обновите транскрипт'
ADD_TRANSCRIPT = 'Пожалуйста, прикрепите транскрипт'
FAILED_TO_VERIFY = 'Модерации не удалось удостоверить ваши данные'
VEFIRY_ACCOUNT = 'Пожалуйста, подтвердите почту'
MESSAGE_FROM_MODERATOR = 'Другая причина'
NO_REASON = 'Без причины'

REVIEW_DECLINE_REASONS = (
    (NO_REASON, 'Еще не отказан'),
    (UPDATE_TRANSCRIPT, 'Обновите транскрипт'),
    (ADD_TRANSCRIPT, 'Прикрепите транскрипт'),
    (FAILED_TO_VERIFY, 'Не удалось удостоверить данные'),
    (VEFIRY_ACCOUNT, 'Почта не подтверждена'),
    (MESSAGE_FROM_MODERATOR, 'Другая причина')
)
OCENIKA = 'ocenika.com'
EMAIL_DECLINE_HEADER = '<p> Ваш отзыв о преподавателе {}, к сожалению был отказан </p>' \
                        '<p> Причина отказа: {} </p>'
EMAIL_ACCEPT_HEADER = '<p>Ваш отзыв о преподавателе {}, успешно прошел модерацию </p>'

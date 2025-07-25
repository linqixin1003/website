# 批量翻译ru目录下的HTML文件为俄语
# 保持格式和排版不变，只翻译文本内容

# 英文到俄语的翻译映射
$translations = @{
    # 通用词汇
    "Getting Started" = "Начало работы"
    "Essential Equipment" = "Необходимое оборудование"
    "Identification Techniques" = "Техники идентификации"
    "Best Locations" = "Лучшие места"
    "Behavior Observation" = "Наблюдение за поведением"
    "Song Identification" = "Идентификация песен"
    "Photography Tips" = "Советы по фотографии"
    "Seasonal Guide" = "Сезонный гид"
    "Journal Keeping" = "Ведение журнала"
    "Ethics and Conservation" = "Этика и охрана природы"
    
    # Pet Care 相关
    "Choosing Right Bird" = "Выбор подходящей птицы"
    "Nutrition and Feeding" = "Питание и кормление"
    "Housing and Environment" = "Жилье и окружающая среда"
    "Health and Veterinary" = "Здоровье и ветеринария"
    "Training and Behavior" = "Дрессировка и поведение"
    "Breeding and Reproduction" = "Разведение и размножение"
    "Emergency First Aid" = "Экстренная первая помощь"
    "Seasonal Care" = "Сезонный уход"
    "Enrichment Activities" = "Обогащающие активности"
    "Senior Bird Care" = "Уход за пожилыми птицами"
    "Species Profiles" = "Профили видов"
    
    # 常见短语
    "Bird Welfare First" = "Благополучие птиц прежде всего"
    "Habitat Protection" = "Защита среды обитания"
    "Respect Others" = "Уважение к другим"
    "Responsible Field Behavior" = "Ответственное полевое поведение"
    "Photography Ethics" = "Этика фотографии"
    "Conservation Action" = "Природоохранные действия"
    "Citizen Science" = "Гражданская наука"
    "Support Organizations" = "Поддержка организаций"
    "Advocacy" = "Адвокация"
    "Sharing Information Responsibly" = "Ответственное распространение информации"
    "Climate Change and Birds" = "Изменение климата и птицы"
    
    # 状态和级别
    "Beginner" = "Начинающий"
    "Intermediate" = "Средний"
    "Advanced" = "Продвинутый"
    "Expert" = "Эксперт"
    "Low" = "Низкий"
    "Moderate" = "Умеренный"
    "High" = "Высокий"
    "Very High" = "Очень высокий"
    
    # 护理相关
    "Care Level" = "Уровень ухода"
    "Noise Level" = "Уровень шума"
    "Care Requirements" = "Требования по уходу"
    "Beginner-Friendly Species" = "Виды для начинающих"
    "Intermediate Species" = "Виды среднего уровня"
    "Advanced Species" = "Продвинутые виды"
    "Choosing the Right Species" = "Выбор подходящего вида"
    
    # 健康相关
    "Finding an Avian Veterinarian" = "Поиск орнитологического ветеринара"
    "Regular Health Monitoring" = "Регулярный мониторинг здоровья"
    "Preventive Care Schedule" = "График профилактического ухода"
    "Common Health Issues" = "Распространенные проблемы со здоровьем"
    "Emergency Situations" = "Экстренные ситуации"
    "Quarantine Procedures" = "Процедуры карантина"
    
    # 行为和训练
    "Understanding Bird Aging" = "Понимание старения птиц"
    "Common Age-Related Health Issues" = "Распространенные возрастные проблемы со здоровьем"
    "Physical Appearance" = "Физический вид"
    "Behavior and Activity" = "Поведение и активность"
    
    # 通用短语
    "Back Button" = "Кнопка назад"
    "Hero Image" = "Главное изображение"
    "Main Content" = "Основное содержание"
    "Visit Before You Decide" = "Посетите перед принятием решения"
    "Special Considerations" = "Особые соображения"
    "Emergency Preparedness" = "Готовность к чрезвычайным ситуациям"
    "Never Give Birds" = "Никогда не давайте птицам"
    "Vet Selection Tip" = "Совет по выбору ветеринара"
    "Personal Actions" = "Личные действия"
    "Playback Guidelines" = "Рекомендации по воспроизведению"
    "Digital vs. Physical Guides" = "Цифровые против физических гидов"
    "Field Guides and Reference Materials" = "Полевые гиды и справочные материалы"
    "Signs of Bird Distress" = "Признаки беспокойства птиц"
}

function Translate-Text {
    param([string]$text)
    
    if ([string]::IsNullOrEmpty($text)) {
        return $text
    }
    
    # 翻译文本
    foreach ($key in $translations.Keys) {
        $text = $text -replace [regex]::Escape($key), $translations[$key]
    }
    
    return $text
}

function Process-HtmlFile {
    param([string]$filePath)
    
    Write-Host "处理文件: $filePath"
    
    try {
        # 读取文件内容
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # 确保语言属性是俄语
        $content = $content -replace '<html lang="[^"]*"', '<html lang="ru"'
        
        # 翻译内容
        $originalContent = $content
        $content = Translate-Text -text $content
        
        # 只有内容发生变化时才写入文件
        if ($content -ne $originalContent) {
            $content | Out-File -FilePath $filePath -Encoding UTF8 -NoNewline
            Write-Host "✅ 已更新: $filePath" -ForegroundColor Green
        } else {
            Write-Host "⏭️  无需更新: $filePath" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host "❌ 处理文件 $filePath 时出错: $($_.Exception.Message)" -ForegroundColor Red
    }
}

# 主函数
Write-Host "开始批量翻译ru目录下的HTML文件..." -ForegroundColor Cyan

# 检查ru目录是否存在
if (-not (Test-Path "ru")) {
    Write-Host "❌ ru目录不存在!" -ForegroundColor Red
    exit
}

# 获取ru目录下的所有HTML文件
$htmlFiles = Get-ChildItem -Path "ru" -Filter "*.html" -Recurse

if ($htmlFiles.Count -eq 0) {
    Write-Host "❌ 在ru目录下没有找到HTML文件!" -ForegroundColor Red
    exit
}

Write-Host "找到 $($htmlFiles.Count) 个HTML文件" -ForegroundColor Green

# 处理每个文件
foreach ($file in $htmlFiles) {
    Process-HtmlFile -filePath $file.FullName
}

Write-Host "`n✅ 批量翻译完成! 共处理了 $($htmlFiles.Count) 个文件" -ForegroundColor Green

Write-Host "`n翻译完成!" -ForegroundColor Green
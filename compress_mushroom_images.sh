#!/bin/bash

# 压缩蘑菇图片为 WebP 格式并居中裁剪为 4:3 比例

IMAGES_DIR="/Users/infno/Documents/work-code/bird-web/website/mushroom/images"
TEMP_DIR="${IMAGES_DIR}/temp"

echo "🍄 开始压缩蘑菇图片..."
echo "📁 图片目录: $IMAGES_DIR"
echo "================================================================================"

# 创建临时目录
mkdir -p "$TEMP_DIR"

# 计数器
count=0
success=0
total_original=0
total_compressed=0

# 处理所有 jpg 文件
for jpg_file in "$IMAGES_DIR"/*.jpg; do
    [ -e "$jpg_file" ] || continue
    
    count=$((count + 1))
    filename=$(basename "$jpg_file")
    name="${filename%.*}"
    webp_file="${IMAGES_DIR}/${name}.webp"
    temp_file="${TEMP_DIR}/${name}_cropped.jpg"
    
    echo ""
    echo "[$count] $filename"
    
    # 获取原始文件大小
    original_size=$(stat -f%z "$jpg_file")
    original_mb=$(echo "scale=2; $original_size / 1048576" | bc)
    total_original=$((total_original + original_size))
    echo "  📦 原始大小: ${original_mb} MB"
    
    # 获取图片尺寸
    dimensions=$(sips -g pixelWidth -g pixelHeight "$jpg_file" | tail -2 | awk '{print $2}')
    width=$(echo "$dimensions" | sed -n 1p)
    height=$(echo "$dimensions" | sed -n 2p)
    
    # 计算 4:3 裁剪尺寸
    target_ratio=1.333333
    current_ratio=$(echo "scale=6; $width / $height" | bc)
    
    if (( $(echo "$current_ratio > $target_ratio" | bc -l) )); then
        # 图片太宽，裁剪宽度
        new_width=$(echo "$height * $target_ratio" | bc | awk '{print int($1)}')
        crop_x=$(echo "($width - $new_width) / 2" | bc | awk '{print int($1)}')
        crop_y=0
        crop_width=$new_width
        crop_height=$height
    else
        # 图片太高，裁剪高度
        new_height=$(echo "$width / $target_ratio" | bc | awk '{print int($1)}')
        crop_x=0
        crop_y=$(echo "($height - $new_height) / 2" | bc | awk '{print int($1)}')
        crop_width=$width
        crop_height=$new_height
    fi
    
    # 居中裁剪为 4:3
    sips --cropToHeightWidth $crop_height $crop_width \
         --cropOffset $crop_y $crop_x \
         "$jpg_file" --out "$temp_file" > /dev/null 2>&1
    
    # 调整大小到最大宽度 1200px
    sips --resampleWidth 1200 "$temp_file" > /dev/null 2>&1
    
    # 转换为 WebP（使用 cwebp 如果可用，否则保持 jpg 并重命名）
    if command -v cwebp &> /dev/null; then
        cwebp -q 85 "$temp_file" -o "$webp_file" > /dev/null 2>&1
        
        # 获取压缩后文件大小
        compressed_size=$(stat -f%z "$webp_file")
        compressed_mb=$(echo "scale=2; $compressed_size / 1048576" | bc)
        total_compressed=$((total_compressed + compressed_size))
        
        compression_ratio=$(echo "scale=1; (1 - $compressed_size / $original_size) * 100" | bc)
        
        echo "  ✅ 压缩后: ${compressed_mb} MB (WebP)"
        echo "  📉 压缩率: ${compression_ratio}%"
        
        # 删除原始文件
        rm "$jpg_file"
        echo "  🗑️  已删除原文件"
        
        success=$((success + 1))
    else
        # 如果没有 cwebp，使用 sips 压缩 JPG
        sips -s format jpeg -s formatOptions 85 "$temp_file" --out "$webp_file" > /dev/null 2>&1
        mv "$webp_file" "${IMAGES_DIR}/${name}.jpg"
        
        compressed_size=$(stat -f%z "${IMAGES_DIR}/${name}.jpg")
        compressed_mb=$(echo "scale=2; $compressed_size / 1048576" | bc)
        total_compressed=$((total_compressed + compressed_size))
        
        compression_ratio=$(echo "scale=1; (1 - $compressed_size / $original_size) * 100" | bc)
        
        echo "  ✅ 压缩后: ${compressed_mb} MB (JPG)"
        echo "  📉 压缩率: ${compression_ratio}%"
        
        # 替换原始文件
        rm "$jpg_file"
        echo "  🗑️  已替换原文件"
        
        success=$((success + 1))
    fi
    
    # 清理临时文件
    rm -f "$temp_file"
done

# 清理临时目录
rm -rf "$TEMP_DIR"

# 总结
echo ""
echo "================================================================================"
echo "🎉 处理完成！"
echo "✅ 成功: $success/$count"

total_original_mb=$(echo "scale=2; $total_original / 1048576" | bc)
total_compressed_mb=$(echo "scale=2; $total_compressed / 1048576" | bc)
total_compression=$(echo "scale=1; (1 - $total_compressed / $total_original) * 100" | bc)
saved_mb=$(echo "scale=2; ($total_original - $total_compressed) / 1048576" | bc)

echo "📦 原始总大小: ${total_original_mb} MB"
echo "📦 压缩后总大小: ${total_compressed_mb} MB"
echo "📉 总压缩率: ${total_compression}%"
echo "💾 节省空间: ${saved_mb} MB"

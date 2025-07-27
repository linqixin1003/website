#!/usr/bin/env python3
import os
import re
from pathlib import Path

def check_german_articles():
    """检查德语文章中的非德语内容"""
    
    de_dir = Path('de')
    if not de_dir.exists():
        print("德语目录不存在")
        return
    
    # 常见的英语单词和短语
    english_patterns = [
        r'\b(the|and|or|but|with|from|this|that|these|those|are|is|was|were|have|has|had|will|would|could|should|may|might|can|must|shall|do|does|did|get|got|make|made|take|took|come|came|go|went|see|saw|know|knew|think|thought|say|said|tell|told|give|gave|find|found|work|worked|call|called|try|tried|ask|asked|need|needed|feel|felt|become|became|leave|left|put|put|mean|meant|keep|kept|let|let|begin|began|seem|seemed|help|helped|talk|talked|turn|turned|start|started|show|showed|hear|heard|play|played|run|ran|move|moved|live|lived|believe|believed|hold|held|bring|brought|happen|happened|write|wrote|provide|provided|sit|sat|stand|stood|lose|lost|pay|paid|meet|met|include|included|continue|continued|set|set|learn|learned|change|changed|lead|led|understand|understood|watch|watched|follow|followed|stop|stopped|create|created|speak|spoke|read|read|allow|allowed|add|added|spend|spent|grow|grew|open|opened|walk|walked|win|won|offer|offered|remember|remembered|love|loved|consider|considered|appear|appeared|buy|bought|wait|waited|serve|served|die|died|send|sent|expect|expected|build|built|stay|stayed|fall|fell|cut|cut|reach|reached|kill|killed|remain|remained|suggest|suggested|raise|raised|pass|passed|sell|sold|require|required|report|reported|decide|decided|pull|pulled)\b',
        r'\b(primary|secondary|tertiary|consumers|producers|predators|prey|ecosystem|ecosystems|habitat|habitats|species|migration|breeding|nesting|foraging|conservation|biodiversity|environmental|ecological|natural|wildlife|population|populations|community|communities|behavior|behaviors|adaptation|adaptations|evolution|evolutionary|genetic|genetics|physiology|physiological|anatomy|anatomical|morphology|morphological|taxonomy|taxonomic|classification|identify|identification|observe|observation|research|study|studies|analysis|data|information|knowledge|science|scientific|biology|biological|ornithology|ornithological|avian|bird|birds|feather|feathers|wing|wings|flight|flying|song|songs|call|calls|nest|nests|egg|eggs|chick|chicks|juvenile|juveniles|adult|adults|male|males|female|females|territory|territories|mating|reproduction|reproductive|seasonal|seasons|winter|spring|summer|autumn|fall|climate|weather|temperature|temperatures|food|feeding|diet|nutrition|nutritional|hunting|hunt|hunted|water|aquatic|terrestrial|arboreal|nocturnal|diurnal|migratory|resident|endemic|native|introduced|invasive|threatened|endangered|extinct|protection|protect|protected|preserve|preservation|restore|restoration|manage|management|monitor|monitoring|survey|surveys|count|counting|census|distribution|range|ranges|abundance|density|rarity|common|uncommon|rare|frequent|occasional|regular|irregular|stable|declining|increasing|fluctuating)\b',
        r'\b(forest|forests|woodland|woodlands|grassland|grasslands|wetland|wetlands|desert|deserts|mountain|mountains|coastal|marine|freshwater|saltwater|river|rivers|lake|lakes|pond|ponds|stream|streams|ocean|oceans|sea|seas|island|islands|continent|continents|tropical|temperate|arctic|alpine|urban|suburban|rural|agricultural|farmland|park|parks|garden|gardens|reserve|reserves|sanctuary|sanctuaries|refuge|refuges|national|international|global|local|regional|area|areas|zone|zones|site|sites|location|locations|place|places|region|regions|country|countries|state|states|province|provinces|city|cities|town|towns|village|villages)\b'
    ]
    
    issues_found = []
    
    print("检查德语文章中的英语内容...")
    
    for html_file in de_dir.rglob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 移除HTML标签和CSS样式，只检查文本内容
            text_content = re.sub(r'<[^>]+>', ' ', content)
            text_content = re.sub(r'style="[^"]*"', ' ', text_content)
            text_content = re.sub(r'class="[^"]*"', ' ', text_content)
            
            english_matches = []
            for pattern in english_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    english_matches.extend(matches)
            
            if english_matches:
                # 去重并统计
                unique_matches = list(set(english_matches))
                issues_found.append({
                    'file': str(html_file),
                    'english_words': unique_matches[:20],  # 只显示前20个
                    'total_count': len(english_matches)
                })
                
                print(f"\n❌ {html_file}")
                print(f"   发现 {len(english_matches)} 个英语单词")
                print(f"   示例: {', '.join(unique_matches[:10])}")
                
        except Exception as e:
            print(f"❌ 处理文件 {html_file} 时出错: {e}")
    
    print(f"\n=== 检查结果 ===")
    print(f"发现 {len(issues_found)} 个文件包含英语内容")
    
    if issues_found:
        print("\n需要翻译的文件:")
        for issue in issues_found:
            print(f"- {issue['file']} ({issue['total_count']} 个英语单词)")
    
    return issues_found

if __name__ == "__main__":
    check_german_articles()
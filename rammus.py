game=discord.Game("람머스 도움")
import discord
import random
import pickle
import asyncio
from discord.ext import commands



bot=commands.Bot(command_prefix='람머스 ')
game=discord.Game("람머스 도움")

token=("your token")

lotto = [4, 7, 9, 17, 26, 38]
lotto_bonus = 20

@bot.event
async def on_ready():
    print('람머스 봇 준비 완료')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title="람머스 봇", description="자세한 사항은 직접 입력해 보세요!", color=0x00d8ff)
    embed.add_field(name="람머스 서버", value="람머스 서버 정보", inline=False)
    embed.add_field(name="람머스 대화", value="람머스와 대화하기! (미완성)", inline=False)
    embed.add_field(name="람머스 롤기능", value="람머스의 롤기능(이건 그냥만들어봄. 경호봇쓰셈ㅋㅋ)", inline=False)
    embed.add_field(name="람머스 돈", value="람머스 서버의 메인!! 돈 시스템 추가", inline=False)
    embed.add_field(name="람머스 미니게임", value="람머스 돈을 얻거나 기타 미니게임! (미완성)", inline=False)
    embed.add_field(name="람머스 도박", value="손쉽게 돈을 얻고싶나? 재밌어질거야..", inline=False)
    embed.add_field(name="람머스 문의", value="버그 제보 & 의견 제시", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 서버(ctx):
    embed = discord.Embed(title="람머스 서버", description="람머스 서버 정보", color=0x00d8ff)
    embed.add_field(name="람머스 시즌", value="람머스의 시즌일 안내", inline=False)
    embed.add_field(name="람머스 패치노트", value="전 시즌과 달라진 사항 안내", inline=False)
    embed.add_field(name="람머스 프로그램", value="람머스를 만들며 사용한 프로그램 안내(TMI)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 대화(ctx):
    embed = discord.Embed(title="람머스 서버", description="람머스 대화 정보", color=0x00d8ff)
    embed.add_field(name="람머스 (기본적인 대사)", value="미완성", inline=False)
    embed.add_field(name="람머스 (롤 챔프)", value="미완성", inline=False)
    embed.add_field(name="람머스 호감도", value="미완성", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 롤기능(ctx):
    embed = discord.Embed(title="람머스 서버", description="람머스 롤기능 정보", color=0x00d8ff)
    embed.add_field(name="람머스 라인정하기", value="람머스가 직접 라인을 정해드립니다!", inline=False)
    embed.add_field(name="람머스 (롤 챔프)", value="람머스가 직접 팀을 나눠드립니다!", inline=False)
    embed.add_field(name="람머스 전적검색", value="미완성(크롤링을 배워오겠어요!)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 돈(ctx):
    embed = discord.Embed(title="람머스 서버", description="람머스 돈 정보", color=0x00d8ff)
    embed.add_field(name="람머스 가입", value="람머스 서버에 가입하여 기본자금(노란색두장)을 얻어가세요!", inline=False)
    embed.add_field(name="람머스 내돈", value="자신의 현재 자산 표시.", inline=False)
    embed.add_field(name="람머스 돈줘", value="1000원 이하 유저에게는 10000원을 드립니다.", inline=False)
    embed.add_field(name="람머스 은행", value="요잇#1356으로 갠톡 주세요. 첫일은 무이자, 이틀째부터 일당 이자 10%씩입니다.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 미니게임(ctx):
    embed = discord.Embed(title="람머스 ", description="람머스 미니게임 정보", color=0x00d8ff)
    embed.add_field(name="람머스 숫자맞추기", value="람머스가 제시하는 1부터 100까지의 숫자를 맞춰보세요! (미완성)", inline=False)
    embed.add_field(name="람머스 상식퀴즈", value="미완성", inline=False)
    embed.add_field(name="람머스 게임퀴즈", value="미완성", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 도박(ctx):
    embed = discord.Embed(title="람머스 서버", description="람머스 도박 정보", color=0x00d8ff)
    embed.add_field(name="람머스 로또", value="5자리 숫자를 맞춰 대박을 노려보세요!", inline=False)
    embed.add_field(name="람머스 즉석복권 & 미니즉석복권", value="즉석으로 최대 15억을 가져갈 수 있는 기회?", inline=False)
    embed.add_field(name="람머스 모아니면도", value="2배씩 증가하는 나의 돈.. 고?, 스톱? (미완성)", inline=False)
    embed.add_field(name="람머스 확률게임", value="2배? 또는 1/2배?, 최대 1000배까지 노려볼 수 있습니다:)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 문의(ctx):
    embed = discord.Embed(title="람머스 서버", description="람머스 서버 정보", color=0x00d8ff)
    embed.add_field(name="버그 제보는?", value="요잇#1356으로 갠톡 주세요.", inline=False)
    embed.add_field(name="버그제보 포상은?", value="중요도에 따라 5만원에서 최대 70만원까지 드립니다.", inline=False)
    embed.add_field(name="그 이외 문의는?", value="시스템 & 기능에 아이디어, 문제점이 있다면 역시 갠톡 주세요.", inline=False)
    await ctx.send(embed=embed)



@bot.command()
async def 로또번호(ctx):
    embed = discord.Embed(title="2월 1주차 콩벌레로또 번호", description="{}  {}  {}  {}  {}  {}   +   {}".format(lotto[0], lotto[1], lotto[2], lotto[3], lotto[4], lotto_bonus), color=0x00d8ff)
    await ctx.send(embed=embed)

@bot.command()
async def 로또(ctx, count):
    try:
        with open("userdata.bin", "rb") as f:
            user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)

    normal = user_data[str(ctx.author.id)]
    for i in range(0, int(count)):
        num_list = []
        for i in range(1, 46):
            num_list.append(i)
        win_num_list = []
        user_data[str(ctx.author.id)] -= 1000
        for i in range(0, 5):
            r_seed = random.randrange(0, len(num_list))
            win_num = num_list.pop(r_seed)
            win_num_list.append(win_num)
        win_num_list.sort()
        await ctx.send(win_num_list)
        point = 0
        for i in range(0, len(win_num_list)):
            for j in range(0, len(lotto)):
                if win_num_list[i] == lotto[j]:
                    point += 1
        point2 = 0
        for i in range(0, len(win_num_list)):
            if win_num_list[i] == lotto_bonus:
                point2 = 1
        if point == 3:
            await ctx.send(ctx.message.author.mention + " 4등,   +50000원! (5만)")
            user_data[str(ctx.author.id)] += 50000
        elif (point == 4) and (point2 == 0):
            await ctx.send(ctx.message.author.mention + " 3등,   +500000원!! (500만)!")
            user_data[str(ctx.author.id)] += 5000000
        elif (point == 4) and (point2 == 1):
            await ctx.send(ctx.message.author.mention + " 2등,   +3000000000원!!! (30억)")
            user_data[str(ctx.author.id)] += 3000000000
        elif point == 5:
            await ctx.send(ctx.message.author.mention + " 1등! 축하드립니다:),  +50000000000원!!!! (500억)")
            user_data[str(ctx.author.id)] += 50000000000

    normal2 = user_data[str(ctx.author.id)]
    nice = normal2 - normal
    await ctx.send('순수익  :  ' + str(nice) + '원')
    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")
    with open("userdata.bin", "wb") as f:
        pickle.dump(user_data, f)


@bot.command()
async def 주사위(ctx):
    dice = random.randint(1,6)
    await ctx.send(dice)

@bot.command()
async def 라인정하기(ctx, *, name):
    line = ["탑", "정글", "미드", "원딜", "서폿"]
    list = []
    user = name.split(" ")
    if len(user) > 5:
        await ctx.send('6명 이상은 안받아요')
    else:
        for i in range(0, len(user)):
            choice = random.choice(line)
            list.append(choice)
            line.remove(choice)
            await ctx.send(choice + "   ->   " + user[i])
            choice = None

@bot.command()
async def 팀정하기(ctx, *, name):
    people_t = name.split(" , ")
    people = people_t[0]
    team = people_t[1]
    person = people.split(" ")
    team_name = team.split(" ")
    random.shuffle(team_name)
    for i in range(0, len(person)):
        await ctx.send(team_name[i] + "   ->   " + person[i])



@bot.command()
async def 즉석복권(ctx, i):
    try:
        with open("userdata.bin", "rb") as f:
            user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)
    i = int(i)
    money_i = 2000*i
    if round(user_data[str(ctx.author.id)]) < int(money_i):
        await ctx.send(ctx.message.author.mention + " 즉석복권 가격은 1개당 2000원입니다. 잔액이 부족합니다.")
        return 0

    if str(ctx.author.id) not in user_data:
        await ctx.send(ctx.message.author.mention + " \"람머스 가입\"으로 가입을 하셔야됩니다.")

    elif i>3000:
        await ctx.send(ctx.message.author.mention + " 즉석복권은 한 번에 1000개만 가능합니다. <1회 2,000,000원 제한>")

    else:
        normal = user_data[str(ctx.author.id)]
        for j in range(i):
            user_data[str(ctx.author.id)] -= 2000
            num1 = random.randint(0, 99)
            num2 = random.randint(0, 99)
            num3 = random.randint(0, 99)
            money = ['30000000', '30000000', '30000000', '30000000', '30000000', '30000000', '30000000', '30000000', '30000000',
                     '30000000', '50000000', '50000000', '50000000', '50000000', '50000000', '50000000', '50000000', '50000000',
                     '100000000', '100000000', '200000000', '300000000', '300000000', '600000000', '1500000000']
            money2 = ['30000', '50000', '70000', '80000', '90000', '100000', '150000', '200000', '250000', '300000']
            g_money = int(random.choice(money))
            g_money2 = int(random.choice(money2))

            await ctx.send(str(num1) + ',  ' + str(num2) + ',  ' + str(num3) + '      ->      ' + str(g_money))
            with open("userdata.bin", "wb") as f:
                pickle.dump(user_data, f)
            if num1 == num2 and num2 == num3:
                user_data[str(ctx.author.id)] += g_money
                await ctx.send(ctx.message.author.mention + ' 잭팟!!   ->   +' + str(g_money) + '원')

            elif str(num1) == str(num2) or str(num2) == str(num3) or str(num1) == str(num3):
                user_data[str(ctx.author.id)] += g_money2
                await ctx.send(ctx.message.author.mention + ' 2개 당첨!   ->   +'  + str(g_money2) + '원')
        normal2 = user_data[str(ctx.author.id)]
        nice = normal2 - normal
        await ctx.send('순수익  :  ' + str(nice) + '원')
        await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")
        with open("userdata.bin", "wb") as f:
            pickle.dump(user_data, f)

@bot.command()
async def 미니즉석복권(ctx, i):
    try:
        with open("userdata.bin", "rb") as f:
            user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)

    i = int(i)
    money_i = 500*i
    if round(user_data[str(ctx.author.id)]) < int(money_i):
        await ctx.send(ctx.message.author.mention + " 미니즉석복권 가격은 1개당 200원입니다. 잔액이 부족합니다.")
        return 0

    if str(ctx.author.id) not in user_data:
        await ctx.send(ctx.message.author.mention + " \"람머스 가입\"으로 가입을 하셔야됩니다.")

    elif i>20:
        await ctx.send(ctx.message.author.mention + " 즉석복권은 한 번에 20개만 가능합니다. <채팅창 도배방지용>")

    else:
        for j in range(i):
            user_data[str(ctx.author.id)] -= 500
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            money = ['20000','20000','20000','40000','40000','40000','60000','120000','300000']
            g_money = int(random.choice(money))

            await ctx.send(str(num1) + ',  ' + str(num2) + '      ->      ' + str(g_money))
            with open("userdata.bin", "wb") as f:
                pickle.dump(user_data, f)
            if num1 == num2:
                user_data[str(ctx.author.id)] += g_money
                await ctx.send(ctx.message.author.mention + ' 당첨!!   ->   +' + str(g_money) + '원')

        await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")
        with open("userdata.bin", "wb") as f:
            pickle.dump(user_data, f)



@bot.command()
async def 숫자맞추기(ctx):
    count = 0
    number = random.randint(1, 99)
    await ctx.send(ctx.message.author.mention + ' 1 부터 99까지 람머스가 생각한 숫자를 10번 안에 맞춰라. 그래.')

    while count < 10:
        count += 1
        await ctx.send('몇 일까요?')
        def check(m):
            return m.author == ctx.author

        user_input = await bot.wait_for('message', check=check)
        if user_input.content.isdigit() is False:
            await ctx.send(ctx.message.author.mention + ' 숫자를 입력하세요.')
            continue

        if int(user_input.content) == number:
            break
        if int(user_input.content) < number:
            await ctx.send(ctx.message.author.mention + " 업")
        if int(user_input.content) > number:
            await ctx.send(ctx.message.author.mention + " 다운")

    if int(user_input.content) == number:
        await ctx.send(ctx.message.author.mention + " 성공!! 람머스가 생각한 숫자는 {} 임.".format(number))
    else:
        await ctx.send(ctx.message.author.mention + " 아, 그것도 못함? ㅋㅋ루빵뽕 람머스가 생각한 숫자는 {} 임.".format(number))


@bot.command()
async def 룰렛(ctx):
    await ctx.send('<0 ~ 999까지 숫자 중 랜덤>')
    number = random.randint(1, 999)

    embed = discord.Embed(title="람모스 룰렛", description=number, color=0x00d8ff)
    await ctx.send(embed=embed)

@bot.command()
async def 모아니면도(ctx):
    s_money = 10000  # start_money
    lv = 1  # level
    finish = False

    while finish == False:
        await ctx.send(ctx.message.author.mention + ' < ' + str(lv) + ' 단계 >')
        await ctx.send(ctx.message.author.mention + ' 현재 돈 : ' + str(s_money) + "원. 성공하면 2배, 실패하면 날아감")
        await ctx.send(ctx.message.author.mention + ' 고 or 스톱?')
        def check(m):
            return m.author == ctx.author
        wait = await bot.wait_for('message', check=check, timeout=10.0)

        if str(wait.content) == '고':
            result = [7, 8]  # 7당첨 8실패
            ohyeah = random.choice(result)
            if ohyeah == 7:
                await ctx.send(ctx.message.author.mention + ' 성공! 돈 x2,   ' + str(s_money) + '원 -> ' + str(s_money * 2) + '원')
                s_money *= 2
                lv += 1
            else:
                await ctx.send(ctx.message.author.mention + ' 실패하셨습니다. 이 돈은 모두 사라집니다.')
                finish = True


        elif str(wait.content) == '스톱':
            await ctx.send(ctx.message.author.mention + ' 스톱하셨습니다. 지금까지 모아놓은 돈을 얻었습니다!')
            await ctx.send(ctx.message.author.mention + ' ' + str(lv) + '단계 스톱, +' + str(s_money) + '원')
            finish = True

        else:
            await ctx.send(ctx.message.author.mention + ' 고(1) or 스톱(2)만 입력해주시기 바랍니다.')


@bot.command()
async def 확률게임(ctx):
    msg = await ctx.send(ctx.message.author.mention + ' 게임을 선택해 주세요!')
    reaction_list = ['2️⃣', '3️⃣', '4️⃣', '5️⃣', '🔟', '🎴', '❌']
    for i in reaction_list:
        await msg.add_reaction(i)
    def check(reaction, m):
        return str(reaction) in reaction_list and m == ctx.author and reaction.message.id == msg.id

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check, timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send(ctx.message.author.mention + ' 시간이 초과되었습니다.')

    if str(reaction) == '2️⃣':
        try:
            with open("userdata.bin", "rb") as f:
                user_data = pickle.load(f)
        except FileNotFoundError:
            with open("userdata.bin", "wb+") as f:
                user_data = dict()
                pickle.dump(user_data, f)

        num = [1, 2]  # 1 당첨 2 실패
        ohyeah = random.choice(num)
        await ctx.send(ctx.message.author.mention + ' 1 & 2 중에 하나 고르던지')

        def check(m):
            return m.author == ctx.author

        msg = await bot.wait_for('message', check=check, timeout=10.0)
        try:
            if msg.content.isdigit() is False:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if int(msg.content) > 2:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if ohyeah == 1:
                await ctx.send(ctx.message.author.mention + ' 석쎅스')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] *= 2

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x2!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")



            elif ohyeah == 2:
                await ctx.send(ctx.message.author.mention + ' 꽝, 다음 기회에..')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] /= 2

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1/2!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")


        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었군그래')


    if str(reaction) == '3️⃣':
        try:
            with open("userdata.bin", "rb") as f:
                user_data = pickle.load(f)
        except FileNotFoundError:
            with open("userdata.bin", "wb+") as f:
                user_data = dict()
                pickle.dump(user_data, f)

        num = [1, 2, 3]  # 1 당첨 2,3 실패
        ohyeah = random.choice(num)
        await ctx.send(ctx.message.author.mention + ' 1 & 2 & 3 중에 하나 고르던지')

        def check(m):
            return m.author == ctx.author

        msg = await bot.wait_for('message', check=check, timeout=10.0)
        try:
            if msg.content.isdigit() is False:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0
            

            if int(msg.content) > 3:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if ohyeah == 1:
                await ctx.send(ctx.message.author.mention + ' 석쎅스')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] *= 5

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x5!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")



            elif ohyeah == 2 or 3:
                await ctx.send(ctx.message.author.mention + ' 꽝, 다음 기회에..')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] /= 3

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1/3!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")


        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었군그래')

    if str(reaction) == '4️⃣':
        try:
            with open("userdata.bin", "rb") as f:
                user_data = pickle.load(f)
        except FileNotFoundError:
            with open("userdata.bin", "wb+") as f:
                user_data = dict()
                pickle.dump(user_data, f)

        num = [1, 2, 3, 4]  # 1 당첨 2,3,4 실패
        ohyeah = random.choice(num)
        await ctx.send(ctx.message.author.mention + ' 1 & 2 & 3 & 4 중에 하나 고르던지')

        def check(m):
            return m.author == ctx.author

        msg = await bot.wait_for('message', check=check, timeout=10.0)
        try:
            if msg.content.isdigit() is False:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if int(msg.content) > 4:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if ohyeah == 1:
                await ctx.send(ctx.message.author.mention + ' 석쎅스')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] *= 8

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x8!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")



            elif ohyeah == 2 or 3 or 4:
                await ctx.send(ctx.message.author.mention + ' 꽝, 다음 기회에..')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] /= 4

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1/4!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")


        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었군그래')

    if str(reaction) == '5️⃣':
        try:
            with open("userdata.bin", "rb") as f:
                user_data = pickle.load(f)
        except FileNotFoundError:
            with open("userdata.bin", "wb+") as f:
                user_data = dict()
                pickle.dump(user_data, f)

        num = [1, 2, 3, 4, 5]  # 1 당첨 2,3,4,5 실패
        ohyeah = random.choice(num)
        await ctx.send(ctx.message.author.mention + ' 1 & 2 & 3 & 4 & 5 중에 하나 고르던지')

        def check(m):
            return m.author == ctx.author

        msg = await bot.wait_for('message', check=check, timeout=10.0)
        try:
            if msg.content.isdigit() is False:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if int(msg.content) > 5:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if ohyeah == 1:
                await ctx.send(ctx.message.author.mention + ' 석쎅스')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] *= 10

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x10!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")



            elif ohyeah == 2 or 3 or 4 or 5:
                await ctx.send(ctx.message.author.mention + ' 꽝, 다음 기회에..')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] /= 5

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1/5!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")


        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었군그래')

    if str(reaction) == '🔟':
        try:
            with open("userdata.bin", "rb") as f:
                user_data = pickle.load(f)
        except FileNotFoundError:
            with open("userdata.bin", "wb+") as f:
                user_data = dict()
                pickle.dump(user_data, f)

        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 1 당첨 2,3,4,5,6,7,8,9,10 실패
        ohyeah = random.choice(num)
        await ctx.send(ctx.message.author.mention + ' 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 중에 하나 고르던지')

        def check(m):
            return m.author == ctx.author

        msg = await bot.wait_for('message', check=check, timeout=10.0)
        try:
            if msg.content.isdigit() is False:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if int(msg.content) > 10:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if ohyeah == 1:
                await ctx.send(ctx.message.author.mention + ' 석쎅스')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] *= 25

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x25!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")



            elif ohyeah == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                await ctx.send(ctx.message.author.mention + ' 꽝, 다음 기회에..')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] /= 10

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1/10!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")


        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었군그래')

    if str(reaction) == '🎴':
        try:
            with open("userdata.bin", "rb") as f:
                user_data = pickle.load(f)
        except FileNotFoundError:
            with open("userdata.bin", "wb+") as f:
                user_data = dict()
                pickle.dump(user_data, f)

        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]  # 1 당첨 2~50 실패
        ohyeah = random.choice(num)
        await ctx.send(ctx.message.author.mention + ' 1 ~ 50 중에 하나 고르던지, 당첨 시 500배, 그 이외 1/50배')

        def check(m):
            return m.author == ctx.author

        msg = await bot.wait_for('message', check=check, timeout=10.0)
        try:
            if msg.content.isdigit() is False:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if int(msg.content) > 50:
                await ctx.send(ctx.message.author.mention + ' 난독증이냐?')
                return 0

            if ohyeah == 1:
                await ctx.send(ctx.message.author.mention + ' 석쎅스, 잭팟!!')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] *= 500

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1000!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")



            elif ohyeah == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48 or 49 or 50:
                await ctx.send(ctx.message.author.mention + ' 꽝, 다음 기회에..')
                if str(ctx.author.id) in user_data:
                    user_data[str(ctx.author.id)] /= 50

                    with open("userdata.bin", "wb") as f:
                        pickle.dump(user_data, f)
                    await ctx.send(ctx.message.author.mention + ' 현재 소유한 자산 x1/50!')
                    await ctx.send(f"{ctx.author.name} 님의 현재 자산 : {round(user_data[str(ctx.author.id)])}원")


        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었군그래')

    if str(reaction) == '❌':
        await ctx.send('취소 되었습니다.')


##아이디어
## 1. 경호 짱돌복권 + 람머스 확률게임
## 2. 둘중에 당첨 -> 천원, 고or스톱, 고 해서 당첨시 2천원, 이런식으로 2배씩 늘려가는 게임.
## 3. 숫자맞추기게임에 돈 넣기 or 숫자야구게임 만들어서 돈 넣기
## 4. 슷랭킹 기능처럼 람랭킹 기능 추가.
## 5. 확률 수정 할거면 수정하기.

@bot.command()
async def 가입(ctx):
    try:
        with open("userdata.bin", "rb") as f:
           user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)

    if str(ctx.author.id) not in user_data:
        user_data[str(ctx.author.id)] = 100000

        with open("userdata.bin", "wb") as f:
            pickle.dump(user_data, f)
        await ctx.send(ctx.message.author.mention + ' 기본자금 10만원 지급되었습니다. 행운을 빌게요ㅎ')

    else:
        await ctx.send(ctx.message.author.mention + ' 이미 가입을 하셨습니다.')


@bot.command()
async def 돈줘(ctx):
    money = 500
    try:
        with open("userdata.bin", "rb") as f:
           user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)

    if str(ctx.author.id) in user_data:
        if user_data[str(ctx.author.id)] < 10000:
            with open("userdata.bin", "wb") as f:
                pickle.dump(user_data, f)
            user_data[str(ctx.author.id)] += 10000
            await ctx.send(ctx.message.author.mention + ' 10000원 지급되었습니다. 좋은 데 쓰세요.')
            with open("userdata.bin", "wb") as f:
                pickle.dump(user_data, f)

        else:
            await ctx.send(ctx.message.author.mention + ' 돈도 많으면서, 바라는게 많군.')

    else:
        await ctx.send(ctx.message.author.mention + ' 먼저 람머스 가입이 필요합니다.')


@bot.command()
async def 내돈(ctx):
    try:
        with open("userdata.bin", "rb") as f:
            user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)

    if str(ctx.author.id) not in user_data:
        user_data[str(ctx.author.id)] = 0
    await ctx.send(f"{ctx.author.name} 님의 자산 : {round(user_data[str(ctx.author.id)])}원")



@bot.command()
@commands.is_owner()
async def 돈줘어드민용(ctx, user_name:discord.Member, amount:int=1000):
    try:
        with open("userdata.bin", "rb") as f:
            user_data = pickle.load(f)
    except FileNotFoundError:
        with open("userdata.bin", "wb+") as f:
            user_data = dict()
            pickle.dump(user_data, f)

    if str(user_name.id) not in user_data:
        user_data[str(user_name.id)] = amount
    else:
        user_data[str(user_name.id)] += amount

    with open("userdata.bin", "wb") as f:
        pickle.dump(user_data, f)

    await ctx.send(f"{user_name.mention} 옛다ㅋㅋ  +{amount}원")

@bot.command()
async def 테스트(ctx):
    await ctx.send(2**7)


@돈줘어드민용.error
async def money_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send(ctx.message.author.mention + ' 이것은 람머스와 혼연일체인 사람만 사용할 수 있음.')


bot.run(token)

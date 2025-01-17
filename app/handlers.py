from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from app import keyboards as kb
import random
from app import tarix as tx

router = Router()
storage = MemoryStorage()

class QuizStates(StatesGroup):
    waiting_for_answer = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"@{message.from_user.username} Salom 👋\n\nSavol javobni boshlash uchun ->  /quiz")

@router.message(F.text == "/quiz")
async def quiz_bot(message: Message, state: FSMContext):
    await message.answer("Python Quiz'ga xush kelibsiz! Sizdan 35 ta savolga javob berishingiz so'raladi.", reply_markup=kb.variant_kb)
    random.shuffle(tx.questions)  # Savollarni aralashtirish
    score = 0  # To'g'ri javoblar soni
    await state.update_data(questions=tx.questions[:35], score=score, current_question=0)
    await ask_question(message, state)

async def ask_question(message: Message, state: FSMContext):
    data = await state.get_data()
    questions = data["questions"]
    current_question = data["current_question"]

    if current_question < len(questions):
        q = questions[current_question]
        options = q["options"].copy()
        random.shuffle(options)

        # Savol va variantlarni chiqarish
        options_text = "\n".join([f"{chr(64 + idx)}. {option}" for idx, option in enumerate(options, start=1)])
        await message.answer(f"\nSavol {current_question + 1}/35: {q['question']}\n{options_text}")

        # Holatni yangilash
        await state.update_data(current_question=current_question + 1, options=options, answer=q["answer"])
        await state.set_state(QuizStates.waiting_for_answer)
    else:
        score = data["score"]
        await message.answer(f"\nSiz {score}/35 ta savolga to'g'ri javob berdingiz! \nDavom etish - /quiz")
        await state.clear()

@router.message(QuizStates.waiting_for_answer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    options = data["options"]
    correct_answer = data["answer"]
    score = data["score"]

    if message.text in ["A", "B", "C", "D"]:
        chosen_option = options[ord(message.text) - 65]
        if chosen_option == correct_answer:
            await message.answer("To'g'ri!")
            score += 1
        else:
            await message.answer(f"Noto'g'ri! To'g'ri javob: {correct_answer}")

        # Holatni yangilash
        await state.update_data(score=score)
        await ask_question(message, state)
    else:
        await message.answer("Iltimos, A, B, C yoki D variantlarini tanlang.")

from fastapi import APIRouter, Depends, File, UploadFile
from loguru import logger
from morpheus_data.database.database import get_db
from morpheus_data.models.schemas import MagicPrompt, Prompt, PromptControlNet

from app.config import get_generative_ai_backend
from app.error.error import ImageNotProvidedError, ModelNotFoundError, UserNotFoundError
from app.integrations.firebase import get_user
from app.models.schemas import Response
from app.services.sdiffusion_services import StableDiffusionService

router = APIRouter()
generative_ai_generator = get_generative_ai_backend()
sd_services = StableDiffusionService(generative_ai_generator=generative_ai_generator)


@router.post(
    "/text2img/prompt/",
    response_description="get image generated by stable diffusion model by a prompt",
)
async def generate_text2img_images(prompt: Prompt = Depends(), db=Depends(get_db), user=Depends(get_user)):
    logger.info(f"Generating text2img images for prompt {prompt} and user {user['email']}")
    try:
        task_id = sd_services.generate_text2img_images(db=db, prompt=prompt, email=user["email"])
        return Response(message="Text2Img request queued successfully", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating text2img images: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.post(
    "/img2img/prompt/",
    response_description="get image generated by stable diffusion model by a prompt and an image",
)
async def generate_img2img_images(
        prompt: Prompt = Depends(),
        image: UploadFile = File(...),
        db=Depends(get_db),
        user=Depends(get_user),
):
    logger.info(f"Generating img2img images for prompt {prompt} and user {user['email']}")
    try:
        image = await image.read()
        task_id = sd_services.generate_img2img_images(db=db, prompt=prompt, image=image, email=user["email"])
        return Response(message="Img2Img request queued successfully", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ImageNotProvidedError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating img2img images: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.post(
    "/controlnet/prompt/",
    response_description="get image generated by stable diffusion model by a prompt with controlnet",
)
async def generate_image_from_prompt_image_controlnet(
        prompt: PromptControlNet = Depends(),
        image: UploadFile = File(...),
        db=Depends(get_db),
        user=Depends(get_user),
):
    logger.info(f"Generating controlnet images for prompt {prompt} and user {user['email']}")
    try:
        image = await image.read()
        task_id = sd_services.generate_controlnet_images(db=db, prompt=prompt, image=image, email=user["email"])
        return Response(message="ControlNet request queued successfully", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ImageNotProvidedError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating controlnet images: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.post(
    "/pix2pix/prompt/",
    response_description="Modify an image with a prompt.",
)
async def generate_pix2pix_from_prompt(
        prompt: Prompt = Depends(),
        image: UploadFile = File(...),
        db=Depends(get_db),
        user=Depends(get_user),
):
    logger.info(f"Generating pix2pix images for prompt {prompt} and user {user['email']}")
    try:
        image = await image.read()
        task_id = sd_services.generate_pix2pix_images(db=db, prompt=prompt, image=image, email=user["email"])
        return Response(message="Pix2Pix request queued successfully.", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ImageNotProvidedError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating pix2pix images: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.post(
    "/inpaint/prompt/",
    response_description="Perform inpainting on an image with a prompt and an image mask.",
)
async def generate_inpaint_from_prompt_and_image_and_mask(
        prompt: Prompt = Depends(),
        image: UploadFile = File(...),
        mask: UploadFile = File(...),
        db=Depends(get_db),
        user=Depends(get_user),
):
    logger.info(f"Generating inpainting images for prompt {prompt} and user {user['email']}")
    try:
        image = await image.read()
        mask = await mask.read()
        task_id = sd_services.generate_inpainting_images(
            db=db, prompt=prompt, image=image, mask=mask, email=user["email"]
        )
        return Response(message="Inpainting request queued successfully.", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ImageNotProvidedError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating inpainting images: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.post(
    "/upscale/prompt/",
    response_description="Perform upscaling on an image with a prompt.",
)
async def generate_upscale_from_prompt_and_image(
        prompt: Prompt = Depends(),
        image: UploadFile = File(...),
        db=Depends(get_db),
        user=Depends(get_user),
):
    logger.info(f"Generating upscaling images for prompt {prompt} and user {user['email']}")
    try:
        image = await image.read()
        task_id = sd_services.generate_upscaling_images(db=db, prompt=prompt, image=image, email=user["email"])
        return Response(message="Upscaling request queued successfully.", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ImageNotProvidedError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating upscaling images: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.post(
    "/magic_prompt/prompt/",
    response_description="Generate better descriptions with a prompt.",
)
async def generate_magic_prompt_from_prompt(prompt: MagicPrompt, user=Depends(get_user)):
    logger.info(f"Generating magic prompt for prompt {prompt} and user {user['email']}")
    try:
        task_id = sd_services.generate_magic_prompt(prompt=prompt, email=user["email"])
        return Response(message="MagicPrompt request queued successfully.", data=task_id)
    except UserNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except ModelNotFoundError as e:
        return Response(success=False, message=str(e), data=None)
    except Exception as e:
        error = f"Something went wrong while generating MagicPrompt: {str(e)}"
        return Response(success=False, message=error, data=None)


@router.get(
    "/results/{task_id}",
    response_description="Get image generation result by task id.",
)
async def get_image_generation_result(task_id, db=Depends(get_db), user=Depends(get_user)):
    try:
        logger.info(f"Getting image generation result for task {task_id} and user {user['email']}")
        generation = sd_services.get_generation_result(db=db, task_id=task_id)
        return Response(message="Image generation result retrieved successfully.", data=generation)
    except Exception as e:
        return Response(success=False, message=str(e), data=None)
